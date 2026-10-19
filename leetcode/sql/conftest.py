"""Runs every sql/lc*.sql file as a test, on DuckDB.

A file holds the query between the `solution` and `tests` marker lines, and below the
`tests` marker the cases, as comments written by scripts/new.py:

    -- schema: Create table If Not Exists World (name varchar(255), ...)
    -- case: {"headers": {...}, "rows": {...}}
    -- expect: {"columns": [...], "rows": [[...]], "ordered": false}

A case whose expected output is not public (premium) has `-- expect: {"run_only": true}`:
the query only has to run.

LeetCode runs MySQL; DuckDB understands most of what these problems need. Backticks, `#`
comments and a handful of MySQL functions (DATEDIFF, DATE_FORMAT, DATE_SUB, IFNULL, IF,
CHAR_LENGTH, GROUP_CONCAT's SEPARATOR) are translated below. Anything else MySQL-only can
make a test fail although LeetCode accepts the query; string comparison is also
case-sensitive here and case-insensitive on MySQL.
"""
import json
import re

import duckdb
import pytest

from _pd import check

TYPES = [(r"^(tiny|small|medium|big)?int", "BIGINT"), (r"^(decimal|numeric|float|double|real)", "DOUBLE"),
         (r"^datetime|^timestamp", "TIMESTAMP"), (r"^date", "DATE"), (r"^(bool|boolean)", "BOOLEAN")]


def pytest_collect_file(parent, file_path):
    if file_path.suffix == ".sql" and file_path.name.startswith("lc"):
        return SqlFile.from_parent(parent, path=file_path)


def parse(text):
    region = re.search(r"-- -+ solution\n(.*?)\n-- -+ tests\n(.*)", text, re.S)
    if not region:
        return "", [], []
    query, tests = region.group(1), region.group(2)
    schema = [m for m in re.findall(r"^-- schema: (.*)$", tests, re.M)]
    cases = [json.loads(m) for m in re.findall(r"^-- case: (.*)$", tests, re.M)]
    expects = [json.loads(m) for m in re.findall(r"^-- expect: (.*)$", tests, re.M)]
    return query, schema, list(zip(cases, expects))


def column_types(schema):
    out = {}
    for ddl in schema:
        m = re.match(r"\s*create table (?:if not exists )?[`\"]?(\w+)[`\"]?\s*\((.*)\)\s*;?\s*$", ddl, re.I | re.S)
        if not m:
            continue
        cols = {}
        for part in re.split(r",(?![^()]*\))", m.group(2)):
            bits = part.strip().split(None, 1)
            if len(bits) == 2:
                t = bits[1].lower()
                cols[bits[0].strip("`\"")] = next((d for p, d in TYPES if re.match(p, t)), "VARCHAR")
        out[m.group(1).lower()] = cols
    return out


MACROS = [
    "CREATE MACRO mysql_datediff(a, b) AS CAST(a AS DATE) - CAST(b AS DATE)",
    "CREATE MACRO mysql_date_sub(d, i) AS d - i",
    "CREATE MACRO mysql_date_add(d, i) AS d + i",
    "CREATE MACRO mysql_if(c, a, b) AS CASE WHEN c THEN a ELSE b END",
]
RENAMES = [(r"\bDATEDIFF\s*\(", "mysql_datediff("), (r"\bDATE_SUB\s*\(", "mysql_date_sub("),
           (r"\bDATE_ADD\s*\(", "mysql_date_add("), (r"\bDATE_FORMAT\s*\(", "strftime("),
           (r"\bIF\s*\(", "mysql_if("), (r"\bCHAR_LENGTH\s*\(", "length("),
           (r"\bGROUP_CONCAT\s*\(", "string_agg("), (r"\s+SEPARATOR\s+", ", ")]


def mysql_to_duckdb(query):
    query = re.sub(r"(?m)(^|(?<=\s))#.*$", "", query)
    query = re.sub(r"(?m)^\s*--.*$", "", query)
    for pat, rep in RENAMES:
        query = re.sub(pat, rep, query, flags=re.I)
    return query.replace("`", '"').strip().rstrip(";")


def run(query, schema, case):
    con = duckdb.connect()
    for m in MACROS:
        con.execute(m)
    types = column_types(schema)
    for table, columns in case["headers"].items():
        t = types.get(table.lower(), {})
        cols = ", ".join(f'"{c}" {t.get(c, "VARCHAR")}' for c in columns)
        con.execute(f'CREATE TABLE "{table}" ({cols})')
        rows = case["rows"].get(table, [])
        if rows:
            con.executemany(f'INSERT INTO "{table}" VALUES ({", ".join("?" * len(columns))})',
                            [[None if v is None else v for v in r] for r in rows])
    return con.execute(mysql_to_duckdb(query)).df()


class SqlFile(pytest.File):
    def collect(self):
        query, schema, cases = parse(self.path.read_text())
        for i, (case, expect) in enumerate(cases, 1):
            yield SqlCase.from_parent(self, name=f"example_{i}", query=query, schema=schema,
                                      case=case, expect=expect)


class SqlCase(pytest.Item):
    def __init__(self, *, query, schema, case, expect, **kw):
        super().__init__(**kw)
        self.query, self.schema, self.case, self.expect = query, schema, case, expect

    def runtest(self):
        q = mysql_to_duckdb(self.query)
        if not q or "TODO: solve" in self.query:
            raise AssertionError("not solved yet")
        got = run(self.query, self.schema, self.case)
        if self.expect.get("run_only"):
            return
        check(got, self.expect["columns"], self.expect["rows"], self.expect.get("ordered", False))

    def reportinfo(self):
        return self.path, 0, self.name
