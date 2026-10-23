#!/usr/bin/env python3
"""Scaffold a LeetCode problem: one file per language, LeetCode's starter code as the
solution, tests generated from the statement's examples.

    scripts/new.py 146                 every language the problem belongs to
    scripts/new.py 146 --lang rust     only that one (rust, cpp, python, pandas, sql)
    scripts/new.py two-sum             a slug works too, plan or not
    scripts/new.py --plan              every plan problem that has no file yet

An existing file is never touched. The stub (`todo!()`, `TODO();`, `raise
NotImplementedError`, `-- TODO: solve`) makes the problem count as unsolved until it
is replaced; the generated tests fail until the solution is right.
"""
from __future__ import annotations

import argparse
import ast
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import leetcode  # noqa: E402
from drills import (ALGO_LANGS, LANGS, ROOT, file_name, load_plan, marker, path,  # noqa: E402
                    plan_label)

CONCURRENCY = {1114, 1115, 1116, 1117, 1188, 1195, 1226, 1242, 1279}
RANDOM_METHOD = re.compile(r"random|pick|shuffle|rand\d", re.I)
RUST_KEYWORDS = {"type", "move", "ref", "loop", "match", "fn", "mod", "impl", "use", "box", "in", "where",
                 "self", "struct", "enum", "trait", "let", "mut", "crate", "super", "as", "dyn"}
CPP_KEYWORDS = {"new", "delete", "class", "default", "and", "or", "not", "xor", "operator", "this", "union",
                "template", "typename", "register", "explicit", "friend", "char", "int", "long", "double"}


# ---------------------------------------------------------------- statement parsing

def statement_text(content: str) -> str:
    h = re.sub(r"<br\s*/?>", "\n", content or "")
    h = re.sub(r"</(p|div|li|pre|ul|ol)>", "\n", h)
    h = re.sub(r"<img[^>]*>", "", h)
    t = re.sub(r"<[^>]+>", "", h)
    return html.unescape(t).replace("\xa0", " ").replace("\r", "")


def outputs(text: str) -> list[str]:
    """Raw text after every 'Output' label, up to the explanation or the next block."""
    out = []
    for m in re.finditer(r"(?m)^\s*Output:?[ \t]*", text):
        rest = text[m.end():]
        stop = re.search(r"\n\s*(Explanation|Example|Constraints|Input|Note|Follow)", rest)
        chunk = rest[: stop.start()] if stop else rest
        out.append(chunk.strip())
    return out


class Unparsed(Exception):
    pass


FAIL = object()


def parse_value(s: str):
    s = s.strip().rstrip(".")
    try:
        return json.loads(s)
    except Exception:
        pass
    try:  # 'True' / single quotes, rarely seen
        return ast.literal_eval(s)
    except Exception:
        return FAIL


def ascii_table(chunk: str):
    lines = [l.strip() for l in chunk.splitlines()]
    rows = [l for l in lines if l.startswith("|")]
    if not rows:
        return None
    cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
    cols, data = cells[0], cells[1:]
    return cols, [[cell(v) for v in r] for r in data]


def cell(v: str):
    if v.lower() == "null":
        return None
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return v


# ---------------------------------------------------------------- signatures

def split_top(s: str) -> list[str]:
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch in "<([{":
            depth += 1
        elif ch in ">)]}":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [x.strip() for x in out if x.strip()]


def rust_fns(code: str) -> dict[str, dict]:
    """{normalised name: {name, params: [(name, type)], ret, self}} from a Rust snippet."""
    out = {}
    for m in re.finditer(r"fn\s+(\w+)\s*(?:<[^>]*>)?\s*\(([^)]*)\)\s*(?:->\s*([^{\n]+?))?\s*(?:where|\{)", code, re.S):
        name, params, ret = m.group(1), m.group(2), (m.group(3) or "()").strip()
        ps, has_self = [], False
        for p in split_top(params):
            if "self" in p and ":" not in p:
                has_self = True
                continue
            n, t = p.split(":", 1)
            ps.append((n.strip(), t.strip()))
        out[norm(name)] = {"name": name, "params": ps, "ret": ret, "self": has_self}
    return out


def cpp_fns(code: str, classname: str) -> dict[str, dict]:
    out = {}
    for m in re.finditer(r"(?m)^[ \t]*(?:([\w:<>,\t \*&]+?)[ \t]+)?(\w+)\s*\(([^)]*)\)\s*(?:const\s*)?\{", code):
        ret, name, params = (m.group(1) or "").strip(), m.group(2), m.group(3)
        if name in ("if", "for", "while", "switch"):
            continue
        ps = []
        for p in split_top(params):
            mm = re.match(r"(.*?)([\w]+)$", p.strip())
            ps.append((mm.group(2), mm.group(1).strip()))
        key = "__init__" if name == classname else norm(name)
        out[key] = {"name": name, "params": ps, "ret": ret or "void"}
    return out


def py_fns(code: str) -> dict[str, dict]:
    out = {}
    for m in re.finditer(r"def\s+(\w+)\s*\((.*?)\)\s*(?:->\s*([^:]+))?:", code, re.S):
        out[norm(m.group(1)) if m.group(1) != "__init__" else "__init__"] = {"name": m.group(1)}
    return out


def norm(name: str) -> str:
    return name.replace("_", "").lower()


def snake(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name).lower()


# Synthesised starter code for premium problems (LeetCode hides the snippets).
def rust_type(t: str) -> str:
    base = {"integer": "i32", "long": "i64", "double": "f64", "boolean": "bool", "string": "String",
            "String": "String", "character": "char", "void": "()", "ListNode": "Option<Box<ListNode>>",
            "TreeNode": "Option<Rc<RefCell<TreeNode>>>"}
    if t.endswith("[]"):
        return f"Vec<{rust_type(t[:-2])}>"
    m = re.fullmatch(r"list<(.+)>", t)
    if m:
        return f"Vec<{rust_type(m.group(1))}>"
    return base[t]


def cpp_type(t: str) -> str:
    base = {"integer": "int", "long": "long long", "double": "double", "boolean": "bool", "string": "string",
            "String": "string", "character": "char", "void": "void", "ListNode": "ListNode*",
            "TreeNode": "TreeNode*"}
    if t.endswith("[]"):
        return f"vector<{cpp_type(t[:-2])}>"
    m = re.fullmatch(r"list<(.+)>", t)
    if m:
        return f"vector<{cpp_type(m.group(1))}>"
    return base[t]


def py_type(t: str) -> str:
    base = {"integer": "int", "long": "int", "double": "float", "boolean": "bool", "string": "str",
            "String": "str", "character": "str", "void": "None", "ListNode": "Optional[ListNode]",
            "TreeNode": "Optional[TreeNode]"}
    if t.endswith("[]"):
        return f"List[{py_type(t[:-2])}]"
    m = re.fullmatch(r"list<(.+)>", t)
    if m:
        return f"List[{py_type(m.group(1))}]"
    return base[t]


def synth(meta: dict, lang: str) -> str:
    def cpp_param(p):
        t = cpp_type(p["type"])
        return f"{t}{'&' if t.startswith(('vector', 'string')) else ''} {p['name']}"

    if "classname" in meta:
        cls, ctor, methods = meta["classname"], meta["constructor"]["params"], meta["methods"]
        if lang == "rust":
            out = [f"struct {cls} {{", "", "}", "", "", f"impl {cls} {{", ""]
            out += [f"    fn new({', '.join(f'{snake(p['name'])}: {rust_type(p['type'])}' for p in ctor)}) -> Self {{",
                    "        ", "    }"]
            for m in methods:
                ps = "".join(f", {snake(p['name'])}: {rust_type(p['type'])}" for p in m["params"])
                ret = rust_type(m["return"]["type"])
                out += ["    ", f"    fn {snake(m['name'])}(&self{ps}){'' if ret == '()' else f' -> {ret}'} {{",
                        "        ", "    }"]
            return "\n".join(out + ["}"])
        if lang == "cpp":
            out = [f"class {cls} {{", "public:", f"    {cls}({', '.join(cpp_param(p) for p in ctor)}) {{", "        ", "    }"]
            for m in methods:
                out += ["    ", f"    {cpp_type(m['return']['type'])} {m['name']}({', '.join(cpp_param(p) for p in m['params'])}) {{",
                        "        ", "    }"]
            return "\n".join(out + ["};"])
        out = [f"class {cls}:", "", f"    def __init__(self{''.join(f', {p['name']}: {py_type(p['type'])}' for p in ctor)}):",
               "        ", ""]
        for m in methods:
            out += [f"    def {m['name']}(self{''.join(f', {p['name']}: {py_type(p['type'])}' for p in m['params'])})"
                    f" -> {py_type(m['return']['type'])}:", "        ", ""]
        return "\n".join(out).rstrip() + "\n"
    name, params, ret = meta["name"], meta["params"], meta.get("return", {"type": "void"})["type"]
    if lang == "rust":
        r = rust_type(ret)
        return "\n".join(["impl Solution {",
                          f"    pub fn {snake(name)}({', '.join(f'{snake(p['name'])}: {rust_type(p['type'])}' for p in params)})"
                          f"{'' if r == '()' else f' -> {r}'} {{", "        ", "    }", "}"])
    if lang == "cpp":
        return "\n".join(["class Solution {", "public:",
                          f"    {cpp_type(ret)} {name}({', '.join(cpp_param(p) for p in params)}) {{", "        ", "    }", "};"])
    return "\n".join(["class Solution:",
                      f"    def {name}(self{''.join(f', {p['name']}: {py_type(p['type'])}' for p in params)}) -> {py_type(ret)}:",
                      "        "])


# ---------------------------------------------------------------- stubs

def stub_rust(code: str) -> str:
    lines = code.split("\n")
    out, pending, done = [], False, False
    openers = []
    for i, l in enumerate(lines):
        if re.search(r"\bfn\s+\w+", l):
            pending = True
        if pending and l.rstrip().endswith("{"):
            openers.append(i)
            pending = False
    for i in openers:
        j = i + 1
        if j < len(lines) and not lines[j].strip():
            k = j + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            closing = k < len(lines) and lines[k].strip().startswith("}")
            indent = re.match(r"\s*", lines[i]).group(0) + "    "
            lines[j] = indent + ("todo!()" if closing else "todo!();")
            done = True
    if not done and openers:
        i = next((o for o in openers if not any("fn new" in x for x in lines[max(o - 3, 0):o + 1])), openers[0])
        indent = re.match(r"\s*", lines[i]).group(0) + "    "
        lines.insert(i + 1, indent + "todo!();")
    return "\n".join(lines)


def stub_cpp(code: str) -> str:
    lines = code.split("\n")
    openers = [i for i, l in enumerate(lines)
               if l.rstrip().endswith("{") and ")" in l and not re.match(r"\s*(class|struct|if|for|while)\b", l)]
    done = False
    for i in openers:
        j = i + 1
        if j < len(lines) and not lines[j].strip():
            lines[j] = re.match(r"\s*", lines[i]).group(0) + "    TODO();"
            done = True
    if not done and openers:
        lines.insert(openers[0] + 1, re.match(r"\s*", lines[openers[0]]).group(0) + "    TODO();")
    return "\n".join(lines)


def stub_py(code: str) -> str:
    lines = code.split("\n")
    i, out, done, first_def = 0, [], False, None
    while i < len(lines):
        l = lines[i]
        out.append(l)
        m = re.match(r"(\s*)def .*:\s*$", l)
        if not m and re.match(r"\s*def ", l) and not l.rstrip().endswith(":"):
            # multi-line signature: copy until the line that ends it
            while i + 1 < len(lines) and not lines[i].rstrip().endswith(":"):
                i += 1
                out.append(lines[i])
            m = re.match(r"(\s*)", l)
        if m:
            indent = m.group(1) + "    "
            first_def = first_def if first_def is not None else len(out)
            j = i + 1
            if j < len(lines) and lines[j].strip().startswith('"""'):
                out.append(lines[j])
                if lines[j].strip().count('"""') == 1:
                    j += 1
                    while j < len(lines) and '"""' not in lines[j]:
                        out.append(lines[j])
                        j += 1
                    if j < len(lines):
                        out.append(lines[j])
                j += 1
                i = j - 1
            k = i + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k >= len(lines) or len(re.match(r"\s*", lines[k]).group(0)) < len(indent) or not lines[k].strip():
                out.append(indent + "raise NotImplementedError")
                done = True
                i = k - 1
        i += 1
    if not done and first_def is not None:
        ind = re.match(r"\s*", out[first_def - 1]).group(0) + "    "
        out.insert(first_def, ind + "raise NotImplementedError")
    return "\n".join(out)


# ---------------------------------------------------------------- literals

def rust_lit(v, t: str) -> str:
    t = t.strip().lstrip("&").replace("mut ", "", 1).strip()
    if t in ("i32", "i64", "usize", "u32", "u64", "isize"):
        return str(int(v))
    if t in ("f64", "f32"):
        s = repr(float(v))
        return s if "." in s or "e" in s else s + ".0"
    if t == "bool":
        return "true" if v else "false"
    if t == "char":
        return "'" + str(v).replace("\\", "\\\\").replace("'", "\\'") + "'"
    if t == "String":
        return json.dumps(str(v), ensure_ascii=False) + ".to_string()"
    if t == "Option<Box<ListNode>>":
        return f"build_list(&[{', '.join(str(x) for x in v)}])"
    if t == "Option<Rc<RefCell<TreeNode>>>":
        return "build_tree(&[" + ", ".join("None" if x is None else f"Some({x})" for x in v) + "])"
    m = re.fullmatch(r"Vec<(.+)>", t)
    if m:
        return "vec![" + ", ".join(rust_lit(x, m.group(1)) for x in v) + "]"
    m = re.fullmatch(r"Option<(.+)>", t)
    if m:
        return "None" if v is None else f"Some({rust_lit(v, m.group(1))})"
    raise ValueError(f"rust type {t}")


def cpp_bare(t: str) -> str:
    t = re.sub(r"\bconst\b", "", t).replace("&", "").strip()
    return re.sub(r"\s+", " ", t).replace(" *", "*").replace("< ", "<").replace(" >", ">")


def cpp_lit(v, t: str, top: bool = True) -> str:
    t = cpp_bare(t)
    if t in ("int", "long", "long long", "unsigned int", "uint32_t", "int64_t", "size_t"):
        n = int(v)
        if t == "int" and n == -2147483648:
            return "INT_MIN"
        return f"{n}LL" if t in ("long", "long long", "int64_t") and abs(n) > 2**31 else str(n)
    if t == "double" or t == "float":
        s = repr(float(v))
        return s if "." in s or "e" in s else s + ".0"
    if t == "bool":
        return "true" if v else "false"
    if t == "char":
        return "'" + str(v).replace("\\", "\\\\").replace("'", "\\'") + "'"
    if t == "string":
        s = json.dumps(str(v), ensure_ascii=False)
        return f"string({s})" if top else s
    if t == "ListNode*":
        return "build({" + ", ".join(str(x) for x in v) + "})"
    if t == "TreeNode*":
        return "build_tree({" + ", ".join("nullopt" if x is None else str(x) for x in v) + "})"
    m = re.fullmatch(r"vector<(.+)>", t)
    if m:
        inner = "{" + ", ".join(cpp_lit(x, m.group(1), top=False) for x in v) + "}"
        return f"{t}{inner}" if top else inner
    raise ValueError(f"cpp type {t}")


def py_lit(v, t: str) -> str:
    if t == "ListNode":
        return f"build({v!r})"
    if t == "TreeNode":
        return f"build_tree({v!r})"
    if t == "ListNode[]":
        return "[" + ", ".join(f"build({x!r})" for x in v) + "]"
    if t == "double" and isinstance(v, int):
        return repr(float(v))
    return repr(v)


# ---------------------------------------------------------------- per-problem model

class Problem:
    def __init__(self, q: dict, plan_entry: dict | None):
        self.q = q
        self.id = int(q["questionFrontendId"])
        self.slug = q["titleSlug"]
        self.title = q["title"]
        self.meta = json.loads(q["metaData"] or "{}")
        self.plan = plan_entry
        self.file = plan_entry["file"] if plan_entry else file_name(self.id, self.slug)
        self.text = statement_text(q.get("content") or "")
        self.premium = not q.get("content")
        self.snippets = {s["langSlug"]: s["code"] for s in q.get("codeSnippets") or []}
        self.database = bool(self.meta.get("database"))
        self.design = "classname" in self.meta
        self.manual = bool(self.meta.get("manual")) or self.id in CONCURRENCY
        self.any_order = bool(re.search(r"\bany order\b", self.text, re.I))
        self.ordered = bool(re.search(r"\border(ed)? by\b", self.text, re.I)) and not self.any_order
        self.url = f"https://leetcode.com/problems/{self.slug}/"

    def langs(self) -> list[str]:
        if self.plan:
            return list(self.plan["langs"])
        return ["pandas", "sql"] if self.database else ALGO_LANGS

    def snippet(self, lang: str) -> str | None:
        key = {"rust": "rust", "cpp": "cpp", "python": "python3", "pandas": "pythondata", "sql": "mysql"}[lang]
        if key in self.snippets:
            return self.snippets[key].replace("\r", "").rstrip() + "\n"
        if self.database or not self.meta or "name" not in self.meta and "classname" not in self.meta:
            return None
        try:
            return synth(self.meta, lang).rstrip() + "\n"
        except Exception:
            return None

    def examples(self):
        """[(inputs: list, output)] or (None, reason)."""
        if self.manual:
            return None, "LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness)"
        cases = self.q.get("exampleTestcaseList") or []
        if not cases:
            return None, "the problem has no example inputs"
        if self.premium:
            outs = [None] * len(cases)
        else:
            outs = outputs(self.text)
            if len(outs) != len(cases):
                return None, f"{len(cases)} example inputs but {len(outs)} outputs in the statement"
        out = []
        for c, o in zip(cases, outs):
            if self.database:
                out.append((json.loads(c), ascii_table(o) if o is not None else None))
                continue
            vals = [parse_value(x) for x in c.split("\n")]
            out.append((vals, None if o is None else parse_value(o)))
        return out, None


# ---------------------------------------------------------------- headers

def header(p: Problem, c: str, extra: list[str] = ()) -> list[str]:
    lines = [f"{p.id}. {p.title} · {p.q['difficulty']} · {p.url}", f"Plan: {plan_label(p.plan)}", "",
             "Problem:", "Approach:", "Time O(?), space O(?)", *extra]
    if c == '"""':
        return ['"""', *lines, '"""']
    return [f"{c} {l}".rstrip() for l in lines]


def no_tests(reason: str, c: str) -> list[str]:
    if reason.startswith("PARTIAL "):
        return [f"{c} Some examples were left out ({reason[8:]}).", ""]
    return [f"{c} No tests were generated: {reason}.", f"{c} Write your own below if you want a local check.", ""]


# ---------------------------------------------------------------- rust

def gen_rust(p: Problem) -> str | None:
    code = p.snippet("rust")
    if code is None:
        return None
    code = re.sub(r"(?m)^(struct \w+ \{[^}]*\n)\};", r"\1}", code)  # LeetCode's own `struct X { };` does not compile
    code = stub_rust(code)
    above = header(p, "//") + ["", "#[allow(unused_imports)]", "use leetcode::*;", ""]
    if "impl Solution" in code and not re.search(r"(?m)^\s*(pub )?struct Solution\b", code):
        above += ["struct Solution;", ""]
    if "rand7()" in code:
        above += ["// LeetCode provides rand7(); this one stands in for it.", "fn rand7() -> i32 {",
                  "    rand::random_range(1..=7)", "}", ""]
    tests, reason = rust_tests(p, code)
    body = [marker("rust", "solution"), code.rstrip(), marker("rust", "tests"), "", "fn main() {}", ""]
    if reason:
        body += no_tests(reason, "//")
    if tests:
        body += ["#[cfg(test)]", "mod tests {", "    use super::*;", ""] + tests + ["}"]
    return "\n".join(above + body).rstrip() + "\n"


def rust_compare(got: str, want, rtype: str, p: Problem, method: str = "") -> list[str]:
    rt = rtype.strip()
    if rt == "Option<Box<ListNode>>":
        return [f"let want: Vec<i32> = {rust_lit(want, 'Vec<i32>')};", f"assert_eq!(list_to_vec(&{got}), want);"]
    if rt == "Option<Rc<RefCell<TreeNode>>>":
        return [f"let want: Vec<Option<i32>> = {rust_lit(want, 'Vec<Option<i32>>')};",
                f"assert_eq!(tree_to_vec(&{got}), want);"]
    if rt == "f64":
        return [f"assert!(approx_eq({got}, {rust_lit(want, 'f64')}));"]
    if rt == "Vec<f64>":
        return [f"assert!(approx_eq_vec(&{got}, &{rust_lit(want, rt)}));"]
    lit = rust_lit(want, rt)
    if p.any_order and rt.startswith("Vec<") and "f64" not in rt:
        fn = "sort_outer" if "permutation" in p.slug else "deep_sort"
        return [f"let want: {rt} = {lit};", f"assert_eq!({fn}({got}), {fn}(want));"]
    if rt.startswith("Vec<") or rt == "String":
        return [f"let want: {rt} = {lit};", f"assert_eq!({got}, want);"]
    return [f"assert_eq!({got}, {lit});"]


def rust_tests(p: Problem, code: str):
    ex, reason = p.examples()
    if ex is None:
        return [], reason
    fns = rust_fns(code)

    def one(n, e):
        inputs, want = e[0], e[1]
        body = []
        if p.design:
            ops, args = inputs
            cls = p.meta["classname"]
            ctor = fns["new"]
            body.append(f"let mut obj = {cls}::new({', '.join(rust_arg(a, t) for a, (_, t) in zip(args[0], ctor['params']))});")
            for i, (op, a) in enumerate(zip(ops[1:], args[1:]), 1):
                f = fns[norm(op)]
                call = f"obj.{f['name']}({', '.join(rust_arg(x, t) for x, (_, t) in zip(a, f['params']))})"
                w = want[i] if isinstance(want, list) and i < len(want) else None
                if w is None or f["ret"] == "()" or RANDOM_METHOD.search(op):
                    body.append(call + ";")
                else:
                    body += rust_compare(call, w, f["ret"], p, op)
        else:
            f = fns[norm(p.meta["name"])]
            if len(inputs) != len(f["params"]):
                raise ValueError("argument count")
            void = f["ret"] == "()"
            args, target = [], None
            for idx, (v, (name, t)) in enumerate(zip(inputs, f["params"])):
                if void and target is None and (t.startswith("&mut") or idx == 0):
                    var = name + "_" if name in RUST_KEYWORDS else name
                    bare = t.lstrip("&").replace("mut ", "", 1).strip()
                    body.append(f"let mut {var}: {bare} = {rust_lit(v, bare)};")
                    args.append(f"&mut {var}" if t.startswith("&mut") else f"&{var}" if t.startswith("&") else var)
                    target = (var, bare)
                else:
                    args.append(rust_arg(v, t))
            call = f"Solution::{f['name']}({', '.join(args)})"
            if want is None or void:
                body.append(call + ";")
            if want is not None:
                body += rust_compare(target[0], want, target[1], p) if void else rust_compare(call, want, f["ret"], p)
        note = ["        // Premium problem: the expected output is not public, so this only runs it."] if p.premium else []
        return ["    #[test]", f"    fn example_{n}() {{"] + note + [f"        {l}" for l in body] + ["    }", ""]

    out, note = drive(p, ex, one, "Rust")
    return out[:-1], note


def drive(p: Problem, ex, one, lang: str):
    """Build every example's test; an example that cannot be generated is left out and named."""
    out, skipped = [], []
    for n, e in enumerate(ex, 1):
        try:
            if has_fail(e):
                raise ValueError("a value in the statement is not plain JSON")
            if e[1] is None and not p.premium:
                raise ValueError("no expected output")
            out += one(n, e)
        except (ValueError, KeyError, TypeError, AttributeError, IndexError) as err:
            skipped.append(f"example {n}: {err}")
    if not out:
        return [], f"could not turn the examples into {lang} ({'; '.join(skipped)})"
    if skipped:
        return out, "PARTIAL " + "; ".join(skipped)
    return out, None


def has_fail(v) -> bool:
    if v is FAIL:
        return True
    if isinstance(v, (list, tuple)):
        return any(has_fail(x) for x in v)
    return False


def rust_arg(v, t: str) -> str:
    if t.startswith("&mut"):
        return f"&mut {rust_lit(v, t)}"
    if t.startswith("&"):
        return f"&{rust_lit(v, t)}"
    return rust_lit(v, t)


# ---------------------------------------------------------------- c++

def gen_cpp(p: Problem) -> str | None:
    code = p.snippet("cpp")
    if code is None:
        return None
    code = stub_cpp(code)
    above = header(p, "//") + ["", '#include "leetcode.hpp"', '#include "test.hpp"', ""]
    if "rand7()" in code:
        above += ["// LeetCode provides rand7(); this one stands in for it.",
                  "inline int rand7() { static mt19937 g(42); return uniform_int_distribution<int>(1, 7)(g); }", ""]
    tests, reason = cpp_tests(p, code)
    body = [marker("cpp", "solution"), code.rstrip(), marker("cpp", "tests"), ""]
    if reason:
        body += no_tests(reason, "//")
    body += tests
    return "\n".join(above + body).rstrip() + "\n"


def cpp_compare(got: str, want, rtype: str, p: Problem) -> str:
    rt = cpp_bare(rtype)
    if rt == "ListNode*":
        return f"CHECK_EQ(to_vector({got}), (vector<int>{cpp_lit(want, 'vector<int>', top=False)}));"
    if rt == "TreeNode*":
        return "CHECK_EQ(to_level_order(" + got + "), (Level{" + ", ".join("nullopt" if x is None else str(x) for x in want) + "}));"
    if rt in ("double", "vector<double>"):
        return f"CHECK(near({got}, {cpp_lit(want, rt)}));"
    lit = cpp_lit(want, rt)
    if p.any_order and rt.startswith("vector<"):
        fn = "sort_outer" if "permutation" in p.slug else "deep_sort"
        return f"CHECK_EQ({fn}({got}), {fn}({lit}));"
    if rt.startswith("vector<") or rt == "string":
        return f"CHECK_EQ({got}, ({lit}));"
    return f"CHECK_EQ({got}, {lit});"


def cpp_tests(p: Problem, code: str):
    ex, reason = p.examples()
    if ex is None:
        return [], reason
    cls = p.meta.get("classname", "Solution")
    fns = cpp_fns(code, cls)

    def one(n, e):
        inputs, want = e[0], e[1]
        body = []
        if p.design:
            ops, args = inputs
            ctor = fns.get("__init__", {"params": []})
            decl, names = cpp_locals(args[0], ctor["params"], "")
            body += decl
            body.append(f"{cls} *obj = new {cls}({', '.join(names)});")
            for i, (op, a) in enumerate(zip(ops[1:], args[1:]), 1):
                f = fns[norm(op)]
                decl, names = cpp_locals(a, f["params"], f"a{i}_")
                call = f"obj->{f['name']}({', '.join(names)})"
                w = want[i] if isinstance(want, list) and i < len(want) else None
                if w is None or cpp_bare(f["ret"]) == "void" or RANDOM_METHOD.search(op):
                    line = call + ";"
                else:
                    line = cpp_compare(call, w, f["ret"], p)
                body += ["{ " + " ".join(decl + [line]) + " }"] if decl else [line]
        else:
            f = fns[norm(p.meta["name"])]
            decl, names = cpp_locals(inputs, f["params"], "")
            body += decl
            call = f"Solution().{f['name']}({', '.join(names)})"
            void = cpp_bare(f["ret"]) == "void"
            if want is None or void:
                body.append(call + ";")
            if want is not None:
                body.append(cpp_compare(names[0], want, f["params"][0][1], p) if void else cpp_compare(call, want, f["ret"], p))
        note = ["    // Premium problem: the expected output is not public, so this only runs it."] if p.premium else []
        return [f"TEST(example_{n}) {{"] + note + [f"    {l}" for l in body] + ["}", ""]

    out, note = drive(p, ex, one, "C++")
    return out[:-1], note


def cpp_locals(values, params, prefix):
    decl, names = [], []
    if len(values) != len(params):
        raise ValueError("argument count")
    for v, (name, t) in zip(values, params):
        var = prefix + name if prefix else (name + "_" if name in CPP_KEYWORDS else name)
        bare = cpp_bare(t)
        if "function<" in bare:
            raise ValueError("callback parameter")
        if prefix and (bare in ("int", "long", "long long", "double", "bool", "char")
                       or bare == "string" and ("&" not in t or "const" in t)):
            names.append(cpp_lit(v, bare, top=False))  # a method's plain value: inline it
            continue
        decl.append(f"{bare} {var} = {cpp_lit(v, bare)};")
        names.append(var)
    return decl, names


# ---------------------------------------------------------------- python

def gen_python(p: Problem) -> str | None:
    code = p.snippet("python")
    if code is None:
        return None
    code = stub_py(code)
    above = header(p, '"""') + ["", "from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)", ""]
    if "rand7()" in code:
        above += ["", "def rand7():  # LeetCode provides it; this one stands in", "    return random.randint(1, 7)", "", ""]
    tests, reason = py_tests(p)
    body = [marker("python", "solution"), code.rstrip(), "", "", marker("python", "tests"), ""]
    if reason:
        body += no_tests(reason, "#")
    body += tests
    return "\n".join(above + body).rstrip() + "\n"


def py_compare(got: str, want, rtype: str, p: Problem) -> str:
    if rtype == "ListNode":
        return f"assert to_list({got}) == {want!r}"
    if rtype == "TreeNode":
        return f"assert to_level_order({got}) == {want!r}"
    if rtype in ("double", "double[]"):
        return f"assert close({got}, {want!r})"
    if p.any_order and isinstance(want, list):
        fn = "sorted" if "permutation" in p.slug else "deep_sorted"
        return f"assert {fn}({got}) == {fn}({want!r})"
    return f"assert {got} == {want!r}"


def py_tests(p: Problem):
    ex, reason = p.examples()
    if ex is None:
        return [], reason

    def one(n, e):
        inputs, want = e[0], e[1]
        body = []
        if p.design:
            ops, args = inputs
            cls = p.meta["classname"]
            ctor = p.meta["constructor"]["params"]
            body.append(f"obj = {cls}({', '.join(py_lit(a, q['type']) for a, q in zip(args[0], ctor))})")
            methods = {m["name"]: m for m in p.meta["methods"]}
            for i, (op, a) in enumerate(zip(ops[1:], args[1:]), 1):
                m = methods[op]
                call = f"obj.{op}({', '.join(py_lit(x, q['type']) for x, q in zip(a, m['params']))})"
                w = want[i] if isinstance(want, list) and i < len(want) else None
                if w is None or m["return"]["type"] == "void" or RANDOM_METHOD.search(op):
                    body.append(call)
                else:
                    body.append(py_compare(call, w, m["return"]["type"], p))
        else:
            params = p.meta["params"]
            ret = p.meta.get("return", {"type": "void"})["type"]
            if len(inputs) != len(params):
                raise ValueError("argument count")
            args = [py_lit(v, q["type"]) for v, q in zip(inputs, params)]
            if ret == "void":
                var = params[0]["name"]
                body.append(f"{var} = {args[0]}")
                args[0] = var
            call = f"Solution().{p.meta['name']}({', '.join(args)})"
            if want is None or ret == "void":
                body.append(call)
            if want is not None:
                body.append(py_compare(params[0]["name"], want, params[0]["type"], p) if ret == "void"
                            else py_compare(call, want, ret, p))
        note = ["    # Premium problem: the expected output is not public, so this only runs it."] if p.premium else []
        return ["", "", f"def test_example_{n}():"] + note + [f"    {l}" for l in body]

    out, note = drive(p, ex, one, "Python")
    return out[2:], note


# ---------------------------------------------------------------- pandas / sql

def table_dtypes(meta: dict) -> dict[str, dict]:
    out = {}
    for line in meta.get("pythondata", []):
        m = re.match(r"\s*(\w+)\s*=\s*pd\.DataFrame\(\[\],\s*columns=\[.*?\]\)\.astype\((\{.*\})\)", line)
        if m:
            try:
                out[m.group(1).lower()] = ast.literal_eval(m.group(2))
            except Exception:
                pass
    return out


def gen_pandas(p: Problem) -> str | None:
    code = p.snippet("pandas")
    if code is None:
        if p.premium and p.meta.get("name"):
            tables = list((p.meta.get("database_schema") or {}).keys())
            code = ("import pandas as pd\n\ndef " + p.meta["name"] + "(" +
                    ", ".join(f"{snake(t)}: pd.DataFrame" for t in tables) + ") -> pd.DataFrame:\n    \n")
        else:
            return None
    code = stub_py(code)
    above = header(p, '"""') + ["", "from _pd import check, frame", ""]
    tests, reason = pandas_tests(p, code)
    body = [marker("pandas", "solution"), code.rstrip(), "", "", marker("pandas", "tests"), ""]
    if reason:
        body += no_tests(reason, "#")
    body += tests
    return "\n".join(above + body).rstrip() + "\n"


def pandas_tests(p: Problem, code: str):
    ex, reason = p.examples()
    if ex is None:
        return [], reason
    m = re.search(r"def\s+(\w+)\s*\((.*?)\)", code, re.S)
    fname, params = m.group(1), [x.split(":")[0].strip() for x in split_top(m.group(2))]
    # LeetCode sometimes names a parameter after the function itself (607:
    # sales_person(sales_person, ...)). Binding the frame to that name in the
    # test would shadow the function before it is called.
    params = [f"{x}_df" if x == fname else x for x in params]
    dtypes = table_dtypes(p.meta)
    out = []
    for n, (case, want) in enumerate(ex, 1):
        tables = list(case["headers"].keys())
        by_norm = {norm(t): t for t in tables}
        body, args = [], []
        for i, prm in enumerate(params):
            t = by_norm.get(norm(prm)) or (tables[i] if i < len(tables) else None)
            if t is None:
                if "argument" in case:
                    args.append(repr(case["argument"]))
                    continue
                return [], f"could not match parameter {prm} to a table"
            cols = case["headers"][t]
            rows = case["rows"].get(t, [])
            types = {c: d for c, d in dtypes.get(t.lower(), {}).items() if c in cols}
            body.append(f"{prm} = frame({cols!r}, {rows!r}, {types!r})")
            args.append(prm)
        call = f"{fname}({', '.join(args)})"
        if want is None:
            if not p.premium:
                return [], "could not read the expected output table"
            body = ["# Premium problem: the expected output is not public, so this only runs it."] + body + [call]
        else:
            cols, rows = want
            body.append(f"check({call}, {cols!r}, {rows!r}, ordered={p.ordered})")
        out += ["", "", f"def test_example_{n}():"] + [f"    {l}" for l in body]
    return out[2:], None


def gen_sql(p: Problem) -> str | None:
    code = p.snippet("sql")
    if code is None:
        if not (p.premium and p.meta.get("mysql")):
            return None
        code = "# Write your MySQL query statement below\n"
    code = code.rstrip() + "\n-- TODO: solve, then delete this line\n"
    above = header(p, "--") + [""]
    ex, reason = p.examples()
    body = [marker("sql", "solution"), code.rstrip(), marker("sql", "tests")]
    if ex is None:
        body += no_tests(reason, "--")
    else:
        body += [f"-- schema: {s}" for s in p.meta.get("mysql", [])]
        for case, want in ex:
            body.append("-- case: " + json.dumps(case, ensure_ascii=False))
            if want is None:
                body.append("-- expect: " + json.dumps({"run_only": True}))
            else:
                body.append("-- expect: " + json.dumps({"columns": want[0], "rows": want[1], "ordered": p.ordered},
                                                       ensure_ascii=False))
    return "\n".join(above + body).rstrip() + "\n"


GEN = {"rust": gen_rust, "cpp": gen_cpp, "python": gen_python, "pandas": gen_pandas, "sql": gen_sql}


# ---------------------------------------------------------------- cli

def resolve(arg: str, plan: dict) -> tuple[str, dict | None]:
    """slug and plan entry for an id or slug."""
    if arg.isdigit():
        pid = int(arg)
        if pid in plan["by_id"]:
            return plan["by_id"][pid]["slug"], plan["by_id"][pid]
        q = leetcode.catalog().get(str(pid))
        if not q:
            sys.exit(f"no LeetCode problem {pid}")
        return q["titleSlug"], None
    slug = arg.strip("/").split("/")[-1]
    entry = next((p for p in plan["problems"] if p["slug"] == slug), None)
    return slug, entry


def scaffold(arg: str, plan: dict, langs: list[str] | None, quiet: bool = False) -> tuple[int, int]:
    slug, entry = resolve(arg, plan)
    p = Problem(leetcode.question(slug), entry)
    made = skipped = 0
    for lang in langs or p.langs():
        dst = path(p.file, lang)
        if dst.exists():
            skipped += 1
            if not quiet:
                print(f"exists, not touching: {dst.relative_to(ROOT)}")
            continue
        text = GEN[lang](p)
        if text is None:
            if not quiet:
                print(f"{p.id} has no {lang} version on LeetCode, skipped")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text)
        made += 1
        print(f"created {dst.relative_to(ROOT)}")
    return made, skipped


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("problems", nargs="*", help="LeetCode ids or slugs")
    ap.add_argument("--lang", help="comma-separated subset of rust,cpp,python,pandas,sql")
    ap.add_argument("--plan", action="store_true", help="every plan problem that has no file yet")
    args = ap.parse_args()
    plan = load_plan()
    langs = args.lang.split(",") if args.lang else None
    if langs and set(langs) - set(LANGS):
        sys.exit(f"unknown language: {', '.join(set(langs) - set(LANGS))}")
    if args.plan:
        made = 0
        for e in plan["problems"]:
            made += scaffold(str(e["id"]), plan, langs, quiet=True)[0]
        print(f"{made} files created")
        return
    if not args.problems:
        ap.error("give a LeetCode id or slug, or --plan")
    total_made = total_skipped = 0
    for a in args.problems:
        m, s = scaffold(a, plan, langs)
        total_made, total_skipped = total_made + m, total_skipped + s
    if total_made == 0 and total_skipped:
        sys.exit(1)


if __name__ == "__main__":
    main()
