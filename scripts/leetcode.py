"""LeetCode's public problem data, cached under .cache/leetcode/<slug>.json.

    question(slug)   statement HTML, starter code per language, signature metadata,
                     example inputs, SQL schema; fetched once, then read from the cache

No login needed: everything here is on the public problem page.
"""
from __future__ import annotations

import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "leetcode"
QUERY = """query q($s: String!) { question(titleSlug: $s) {
  questionFrontendId title titleSlug difficulty isPaidOnly content
  metaData exampleTestcaseList sampleTestCase
  codeSnippets { langSlug code } } }"""


def question(slug: str) -> dict:
    path = CACHE / f"{slug}.json"
    if path.exists():
        return json.loads(path.read_text())
    body = json.dumps({"query": QUERY, "variables": {"s": slug}}).encode()
    req = urllib.request.Request("https://leetcode.com/graphql", data=body, headers={
        "Content-Type": "application/json", "Referer": f"https://leetcode.com/problems/{slug}/",
        "User-Agent": "Mozilla/5.0"})
    for attempt in range(4):
        try:
            q = json.load(urllib.request.urlopen(req, timeout=30))["data"]["question"]
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    if q is None:
        raise SystemExit(f"LeetCode has no problem '{slug}'")
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(q, ensure_ascii=False))
    time.sleep(1)  # be gentle with a public endpoint
    return q


LIST_QUERY = ('query q($skip:Int,$limit:Int){ questionList(categorySlug:"", limit:$limit, skip:$skip, filters:{}) '
              '{ totalNum data { questionFrontendId title titleSlug difficulty isPaidOnly } } }')


def catalog(refresh: bool = False) -> dict[str, dict]:
    """Every problem, by frontend id (as a string): {id: {title, titleSlug, difficulty, isPaidOnly}}."""
    path = CACHE.parent / "problems.json"
    if path.exists() and not refresh:
        return json.loads(path.read_text())
    out, skip = [], 0
    while True:
        body = json.dumps({"query": LIST_QUERY, "variables": {"skip": skip, "limit": 100}}).encode()
        req = urllib.request.Request("https://leetcode.com/graphql", data=body, headers={
            "Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
        data = json.load(urllib.request.urlopen(req, timeout=30))["data"]["questionList"]
        out += data["data"]
        skip += 100
        if skip >= data["totalNum"]:
            break
        time.sleep(1)
    by_id = {q["questionFrontendId"]: q for q in out}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(by_id, ensure_ascii=False))
    return by_id


def snippet(q: dict, lang: str) -> str | None:
    return next((s["code"] for s in q.get("codeSnippets") or [] if s["langSlug"] == lang), None)
