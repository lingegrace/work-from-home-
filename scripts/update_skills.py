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
OUT = pathlib.Path(__file__).resolve().parent.parent / "skills.json"


def get(url, accept="application/vnd.github+json"):
    headers = {"User-Agent": "lingegrace-site-updater", "Accept": accept}
    if os.environ.get("GITHUB_TOKEN") and "api.github.com" in url:
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return r.read().decode("utf-8")


def main():
    try:
        entries = json.loads(get(f"https://api.github.com/repos/{REPO}/contents/skills"))
        skills = []
        for e in sorted((e for e in entries if e["type"] == "dir"), key=lambda e: e["name"]):
            name = e["name"]
            readme = get(f"https://raw.githubusercontent.com/{REPO}/main/skills/{name}/README.md", accept="text/plain")
            lines = [l.strip() for l in readme.splitlines()]
            m = re.match(r"#\s*([^:]+):\s*(.+)", lines[0])
            tagline = m.group(2).strip() if m else ""
            summary = next((l for l in lines[1:] if l and not l.startswith("#")), "")
            summary = re.sub(r"[*_`]", "", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", summary))
            skills.append({"name": name, "tagline": tagline, "summary": summary,
                           "url": f"https://github.com/{REPO}/tree/main/skills/{name}"})
    except Exception as ex:
        print(f"Could not read skills repo: {ex}. Keeping existing file.")
        return 0
    if not skills:
        print("No skills found. Keeping existing file.")
        return 0
    order = ["content-research-analyst", "sociology-deep-research", "competitive-market-research"]
    skills.sort(key=lambda s: order.index(s["name"]) if s["name"] in order else len(order))
    data = {"repo": f"https://github.com/{REPO}", "updated": dt.date.today().isoformat(), "skills": skills}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(skills)} skills: {', '.join(s['name'] for s in skills)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
