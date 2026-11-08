"""Fetch the public LinkedIn newsletter page and write newsletter.json (newest issues first).

Run by .github/workflows/newsletter.yml once a day. If LinkedIn can't be read,
the existing newsletter.json is left untouched so the site keeps working.
"""
import datetime as dt
import html
import json
import pathlib
import re
import sys
import urllib.request

NEWSLETTER_URL = "https://www.linkedin.com/newsletters/7422191016994217984/"
OUT = pathlib.Path(__file__).resolve().parent.parent / "newsletter.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def parse(page):
    """Find every issue link. Attribute order inside the <a> tag doesn't matter (LinkedIn changes it)."""
    issues, seen = [], set()
    for m in re.finditer(r"<a\b([^>]*\bshare-article__title-link\b[^>]*)>\s*([^<]+?)\s*<", page):
        attrs, title = m.group(1), html.unescape(m.group(2)).strip()
        h = re.search(r'href="(https://www\.linkedin\.com/pulse/[^"?]+)', attrs)
        if not h or h.group(1) in seen or not title:
            continue
        url = h.group(1)
        seen.add(url)
        tail = page[m.end():m.end() + 6000]
        d = re.search(r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (\d{1,2}), (20\d\d)", tail)
        date = dt.datetime.strptime(" ".join(d.groups()), "%b %d %Y").date().isoformat() if d else None
        before = page[max(0, m.start() - 2500):m.start()]
        covers = [html.unescape(c) for c in re.findall(r'(?:data-delayed-url|src)="(https://media\.licdn\.com/dms/image/[^"]+)"', before) if "article-cover" in c]
        issues.append({"title": title, "url": url, "date": date, "cover": covers[-1] if covers else None})
    # newest first, keeping LinkedIn's order for undated items
    order = {i["url"]: n for n, i in enumerate(issues)}
    issues.sort(key=lambda i: (i["date"] or "", -order[i["url"]]), reverse=True)
    return issues


def main():
    try:
        page = fetch(NEWSLETTER_URL)
        issues = parse(page)
    except Exception as e:  # network error, LinkedIn block, etc.
        print(f"Could not read newsletter page: {e}. Keeping existing file.")
        return 0
    if not issues:
        print("No issues found on the page (layout changed or blocked). Keeping existing file.")
        return 0
    logo = re.search(r'<meta property="og:image" content="([^"]+)"', page)
    data = {"newsletter": "Signals Across Markets", "url": NEWSLETTER_URL, "logo": html.unescape(logo.group(1)) if logo else None,
            "updated": dt.date.today().isoformat(), "issues": issues[:6]}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(data['issues'])} issues. Latest: {issues[0]['title']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
