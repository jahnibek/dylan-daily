#!/usr/bin/env python3
"""Build one Dylan Daily report and refresh the library home page.

Usage:  python3 tools/build.py content/2026-10-12-jeff-kinney.json
        python3 tools/build.py --index-only

A content file is JSON with:
  meta:   {date: "YYYY-MM-DD", slug, category, emoji, title_plain, teaser}
  page:   {kind, readTime, title (may hold <span class="hl">), sub, bigIdea,
           cards[5]{emo,title,front,back,tryit}, words[3-5]{w,d},
           quiz[4]{q,opts[3],a,hint,why}, think, tries[3-4], footer}
"""
import html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"tennis": "Tennis", "games": "Games", "screen": "Movies & Shows",
        "books": "Books", "anime": "Anime & Manga", "wildcard": "Wildcard",
        "skills": "Skills", "howitworks": "How Stuff Works",
        "mathsci": "Science & Math"}


def fail(msg):
    sys.exit("build.py: " + msg)


def check(c):
    m, p = c.get("meta", {}), c.get("page", {})
    for k in ("date", "slug", "category", "emoji", "title_plain", "teaser"):
        if not m.get(k):
            fail(f"meta.{k} missing")
    if m["category"] not in CATS:
        fail(f"meta.category must be one of {list(CATS)}")
    for k in ("kind", "readTime", "title", "sub", "bigIdea", "think", "footer"):
        if not p.get(k):
            fail(f"page.{k} missing")
    if len(p.get("cards", [])) != 5:
        fail("page.cards must have exactly 5 items")
    if len(p.get("quiz", [])) != 4:
        fail("page.quiz must have exactly 4 items")
    for i, q in enumerate(p["quiz"]):
        if len(q.get("opts", [])) != 3 or q.get("a") not in (0, 1, 2):
            fail(f"quiz {i+1}: needs 3 opts and a in 0..2")
    if [q["a"] for q in p["quiz"]].count(p["quiz"][0]["a"]) == 4:
        fail("vary the position of correct answers")
    if not 3 <= len(p.get("words", [])) <= 5:
        fail("page.words must have 3-5 items")
    if not 3 <= len(p.get("tries", [])) <= 4:
        fail("page.tries must have 3-4 items")


def build_report(path):
    c = json.load(open(path, encoding="utf-8"))
    check(c)
    m, p = c["meta"], c["page"]
    t = open(os.path.join(ROOT, "tools", "template.html"), encoding="utf-8").read()
    data = json.dumps(p, ensure_ascii=False, indent=1).replace("</", "<\\/")
    t = t.replace("/*__DATA__*/", data).replace("__TITLE__", html.escape(m["title_plain"]))
    name = f'{m["date"]}-{m["slug"]}.html'
    open(os.path.join(ROOT, "reports", name), "w", encoding="utf-8").write(t)
    reg_path = os.path.join(ROOT, "data", "reports.json")
    reg = json.load(open(reg_path)) if os.path.exists(reg_path) else []
    reg = [r for r in reg if r["file"] != name]
    reg.insert(0, {"file": name, **{k: m[k] for k in ("date", "slug", "category", "emoji", "title_plain", "teaser")}})
    reg.sort(key=lambda r: r["date"], reverse=True)
    json.dump(reg, open(reg_path, "w"), ensure_ascii=False, indent=1)
    print("built reports/" + name)
    return name


def build_index():
    reg = json.load(open(os.path.join(ROOT, "data", "reports.json")))
    e = html.escape
    cards = "".join(
        f'<a class="r" href="reports/{e(r["file"])}"><span class="em">{r["emoji"]}</span>'
        f'<span class="tx"><span class="meta">{e(CATS[r["category"]])} · {e(r["date"])}</span>'
        f'<b>{e(r["title_plain"])}</b><span class="te">{e(r["teaser"])}</span></span></a>'
        for r in reg)
    latest = reg[0] if reg else None
    hero = (f'<a class="today" href="reports/{e(latest["file"])}"><span class="lbl">Newest report</span>'
            f'<span class="em big">{latest["emoji"]}</span><b>{e(latest["title_plain"])}</b>'
            f'<span class="te">{e(latest["teaser"])}</span><span class="go">Open it →</span></a>') if latest else ""
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Dylan Daily</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
:root{{color-scheme:dark;--bg:#10243D;--card:#1A3252;--card2:#23406A;--ink:#fff;--text:#D6DCE6;--mute:#93A3BA;--orange:#E08A4B;--blue:#5AA9E6}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:Nunito,system-ui,sans-serif;font-size:17px;line-height:1.5}}
.wrap{{max-width:820px;margin:0 auto;padding:28px 16px 64px}}
.tag{{display:inline-block;font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--blue);background:var(--card);padding:5px 12px;border-radius:20px}}
h1{{color:var(--ink);font-size:38px;font-weight:900;margin:12px 0 4px}} h1 span{{color:var(--orange)}}
.sub{{color:var(--mute)}}
.today{{display:flex;flex-direction:column;gap:6px;margin:26px 0 30px;background:var(--card);border-left:6px solid var(--orange);border-radius:16px;padding:20px 22px;text-decoration:none;color:var(--text)}}
.today b{{color:var(--ink);font-size:24px;font-weight:900;line-height:1.2}}
.lbl{{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--orange)}}
.go{{color:var(--blue);font-weight:800;margin-top:4px}}
.em{{font-size:30px;line-height:1}} .em.big{{font-size:40px}}
h2{{color:var(--ink);font-size:22px;font-weight:900;margin-bottom:12px}}
.list{{display:grid;gap:12px}}
.r{{display:flex;gap:14px;align-items:flex-start;background:var(--card);border-radius:14px;padding:14px 16px;text-decoration:none;color:var(--text)}}
.r:hover,.today:hover{{background:var(--card2)}}
.r:focus-visible,.today:focus-visible{{outline:3px solid var(--blue);outline-offset:2px}}
.tx{{display:flex;flex-direction:column;gap:2px;min-width:0}}
.r b{{color:var(--ink);font-size:18px;font-weight:800;line-height:1.25}}
.meta{{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--blue)}}
.te{{font-size:15px;color:var(--mute)}}
footer{{margin-top:40px;text-align:center;color:var(--mute);font-size:14px}}
</style></head><body><div class="wrap">
<span class="tag">For Dylan · a new report every morning</span>
<h1>Dylan <span>Daily</span></h1>
<p class="sub">The stories behind the players, games, shows and books you love.</p>
{hero}
<h2>All reports</h2><div class="list">{cards}</div>
<footer>Made for Dylan by Dad</footer>
</div></body></html>'''
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page)
    print(f"built index.html ({len(reg)} reports)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        fail("give a content file or --index-only")
    if sys.argv[1] != "--index-only":
        for f in sys.argv[1:]:
            build_report(f)
    build_index()
