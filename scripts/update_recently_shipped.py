from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.request import Request, urlopen

START = "<!-- RECENTLY-SHIPPED:START -->"
END = "<!-- RECENTLY-SHIPPED:END -->"

REPOSITORIES = [
    "ShapArt/Matrtix-Cleaner",
    "ShapArt/tessa-matrix-studio",
    "ShapArt/eyegate-l-luckfox-scud",
    "ShapArt/vpn-bot-stars-hiddify",
]

PROJECT_NAMES = {
    "ShapArt/Matrtix-Cleaner": "Matrix Cleaner",
    "ShapArt/tessa-matrix-studio": "TESSA Matrix Studio",
    "ShapArt/eyegate-l-luckfox-scud": "EyeGate-L",
    "ShapArt/vpn-bot-stars-hiddify": "SH4PART VPN",
}


def _first_line(value: str | None, limit: int = 90) -> str:
    text = (value or "").splitlines()[0].strip() if value else ""
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def _date(value: str) -> str:
    return value[:10]


def replace_block(readme: str, generated: str) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one Recently Shipped marker pair")
    start_index = readme.index(START) + len(START)
    end_index = readme.index(END)
    if start_index > end_index:
        raise ValueError("Recently Shipped markers are out of order")
    return readme[:start_index] + "\n" + generated.rstrip("\n") + "\n" + readme[end_index:]


def item_from_release(repo: str, data: dict) -> dict:
    timestamp = data.get("published_at") or data.get("created_at")
    if not timestamp:
        raise ValueError(f"Release for {repo} has no timestamp")
    tag = str(data.get("tag_name") or "release")
    title = _first_line(str(data.get("name") or tag))
    return {
        "repo": repo,
        "name": PROJECT_NAMES.get(repo, repo.rsplit("/", 1)[-1]),
        "url": str(data.get("html_url") or f"https://github.com/{repo}/releases"),
        "label": tag,
        "date": _date(timestamp),
        "title": title,
        "sort_key": timestamp,
    }


def item_from_commit(repo: str, data: dict) -> dict:
    commit = data.get("commit") or {}
    committer = commit.get("committer") or {}
    author = commit.get("author") or {}
    timestamp = committer.get("date") or author.get("date")
    if not timestamp:
        raise ValueError(f"Commit for {repo} has no timestamp")
    sha = str(data.get("sha") or "")[:7]
    title = _first_line(str(commit.get("message") or "update"))
    return {
        "repo": repo,
        "name": PROJECT_NAMES.get(repo, repo.rsplit("/", 1)[-1]),
        "url": str(data.get("html_url") or f"https://github.com/{repo}"),
        "label": sha,
        "date": _date(timestamp),
        "title": title,
        "sort_key": timestamp,
    }


def render_items(items: list[dict]) -> str:
    lines = []
    for item in sorted(items, key=lambda value: value["sort_key"], reverse=True)[:4]:
        lines.append(f'- [{item["name"]}]({item["url"]}) · `{item["label"]}` · {item["date"]}')
    return "\n".join(lines)


def _request_json(url: str, token: str | None = None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "ShapArt-profile-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(url, headers=headers)
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_item(repo: str, token: str | None = None) -> dict:
    release_url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        release = _request_json(release_url, token)
        if release.get("draft") or release.get("prerelease"):
            raise HTTPError(release_url, 404, "No stable release", hdrs=None, fp=None)
        return item_from_release(repo, release)
    except HTTPError as error:
        if error.code != 404:
            raise

    commits_url = f"https://api.github.com/repos/{repo}/commits?per_page=1"
    commits = _request_json(commits_url, token)
    if not commits:
        raise ValueError(f"No public release or commit found for {repo}")
    return item_from_commit(repo, commits[0])


def update_readme(path: str = "README.md", token: str | None = None) -> bool:
    readme_path = Path(path)
    before = readme_path.read_text(encoding="utf-8")
    items = [fetch_item(repo, token) for repo in REPOSITORIES]
    generated = render_items(items)
    after = replace_block(before, generated)
    if after == before:
        return False
    readme_path.write_text(after, encoding="utf-8")
    return True


def main() -> None:
    changed = update_readme(token=os.environ.get("GITHUB_TOKEN"))
    print("README updated" if changed else "README already current")


if __name__ == "__main__":
    main()
