"""Read the skills in github.com/lingegrace/claude-research-skills and write skills.json.

Each skill folder's README.md starts with "# <name>: <tagline>" followed by a one-sentence summary;
that's what the website shows. Run daily by .github/workflows/update-feeds.yml.
If GitHub can't be read, the existing skills.json is kept.
"""
import datetime as dt
import json
import os
import pathlib
import re
import sys
import urllib.request

REPO = "lingegrace/claude-research-skills"
# Shown as full cards on the website; every other skill appears in the short list.
FEATURED = ["value-proposition-writer", "competitive-market-research", "sociology-deep-research"]
OUT = pathlib.Path(__file__).resolve().parent.parent / "skills.json"


def get(url, accept="application/vnd.github+json"):
    headers = {"User-Agent": "lingegrace-site-updater", "Accept": accept}
    if os.environ.get("GITHUB_TOKEN") and "api.github.com" in url:
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return r.read().decode("utf-8")


def main():
    try:
        tree = json.loads(get(f"https://api.github.com/repos/{REPO}/git/trees/main?recursive=1"))["tree"]
        paths = sorted(t["path"] for t in tree if re.fullmatch(r"skills/(?:[^/]+/)?[^/]+/SKILL\.md", t["path"]))
        skills = []
        for path in paths:
            folder = path.rsplit("/", 1)[0]
            parts = folder.split("/")
            name, section = parts[-1], (parts[1] if len(parts) == 3 else "")
            readme = get(f"https://raw.githubusercontent.com/{REPO}/main/{folder}/README.md", accept="text/plain")
            lines = [l.strip() for l in readme.splitlines()]
            m = re.match(r"#\s*([^:]+):\s*(.+)", lines[0])
            tagline = m.group(2).strip() if m else ""
            summary = next((l for l in lines[1:] if l and not l.startswith(("#", "|"))), "")
            summary = re.sub(r"[*_`]", "", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", summary))
            skills.append({"name": name, "section": section, "tagline": tagline, "summary": summary,
                           "url": f"https://github.com/{REPO}/tree/main/{folder}", "featured": name in FEATURED})
    except Exception as ex:
        print(f"Could not read skills repo: {ex}. Keeping existing file.")
        return 0
    if not skills:
        print("No skills found. Keeping existing file.")
        return 0
    sections = ["product-marketing", "sociology", "research", ""]
    preferred = ["value-proposition-writer", "positioning-messaging", "user-persona-builder", "customer-review-mining",
                 "competitive-market-research", "feature-launch-kit", "customer-case-study", "ai-product-audit",
                 "research-question-grill", "sociology-deep-research", "interview-guide", "thematic-analysis",
                 "quantitative-analysis", "content-research-analyst", "fact-check-draft"]
    rank = lambda n: preferred.index(n) if n in preferred else len(preferred)
    skills.sort(key=lambda k: (sections.index(k["section"]) if k["section"] in sections else len(sections), rank(k["name"]), k["name"]))
    data = {"repo": f"https://github.com/{REPO}", "sections": {"product-marketing": "Product & Marketing", "sociology": "Sociology & Social Science", "research": "Research & Writing"}, "updated": dt.date.today().isoformat(), "skills": skills}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(skills)} skills: {', '.join(s['name'] for s in skills)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
