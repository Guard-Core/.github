#!/usr/bin/env python3
"""First-interaction greetings (LEDGER 6.509, D-234), on the repo's own GITHUB_TOKEN with no privileged trigger.

An `issues` event greets that issue's author on their first issue. A scheduled or dispatched run looks back over recent issues and pull
requests, so a pull request opened from a fork (which never gets a write token on `pull_request`) is greeted within the hour. Idempotent:
a hidden marker in the posted comment makes every later pass skip that item. Standard library only; `api` is injected for the tests."""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from collections.abc import Callable
from datetime import datetime, timedelta, timezone

API = "https://api.github.com"
Api = Callable[[str, str, dict | None], object]


def marker(kind: str) -> str:
    return f"<!-- guard-core-greeting:{kind} -->"


def http_api(token: str) -> Api:
    def api(method: str, path: str, body: dict | None = None) -> object:
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(
            API + path,
            data=data,
            method=method,
            headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)

    return api


def paged(api: Api, path: str) -> list[dict]:
    items: list[dict] = []
    page = 1
    sep = "&" if "?" in path else "?"
    while True:
        chunk = api("GET", f"{path}{sep}per_page=100&page={page}", None)
        if not isinstance(chunk, list):
            raise ValueError(f"unexpected response for {path}")
        items.extend(chunk)
        if len(chunk) < 100:
            return items
        page += 1


def is_bot(user: dict) -> bool:
    return user.get("type") == "Bot" or str(user.get("login", "")).endswith("[bot]")


def kind_of(item: dict) -> str:
    return "pr" if "pull_request" in item else "issue"


def should_greet(api: Api, repo: str, item: dict) -> bool:
    kind = kind_of(item)
    if is_bot(item["user"]):
        return False
    comments = paged(api, f"/repos/{repo}/issues/{item['number']}/comments")
    if any(marker(kind) in (c.get("body") or "") for c in comments):
        return False
    theirs = paged(api, f"/repos/{repo}/issues?state=all&creator={item['user']['login']}")
    earlier = [i for i in theirs if kind_of(i) == kind and i["number"] < item["number"]]
    return not earlier


def greet(api: Api, repo: str, item: dict, messages: dict[str, str]) -> bool:
    kind = kind_of(item)
    text = messages.get(kind, "").strip()
    if not text or not should_greet(api, repo, item):
        return False
    api("POST", f"/repos/{repo}/issues/{item['number']}/comments", {"body": f"{text}\n\n{marker(kind)}"})
    return True


def recent_items(api: Api, repo: str, since: datetime) -> list[dict]:
    """Issues and pull requests created since `since`, oldest first (the issues endpoint lists both)."""
    stamp = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    items = paged(api, f"/repos/{repo}/issues?state=all&sort=created&direction=desc&since={stamp}")
    fresh = [i for i in items if datetime.strptime(i["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) >= since]
    return sorted(fresh, key=lambda i: i["number"])


def run(api: Api, repo: str, event_name: str, event: dict, messages: dict[str, str], now: datetime, lookback_hours: int) -> list[int]:
    if event_name == "issues":
        candidates = [event["issue"]] if event.get("action") == "opened" else []
    else:
        candidates = recent_items(api, repo, now - timedelta(hours=lookback_hours))
    return [item["number"] for item in candidates if greet(api, repo, item, messages)]


def main() -> int:
    token = os.environ.get("GH_TOKEN", "")
    repo = os.environ.get("REPO", "")
    if not token or not repo:
        print("::error::GH_TOKEN and REPO are required")
        return 2
    event_name = os.environ.get("EVENT_NAME", "")
    event: dict = {}
    if event_name == "issues":
        with open(os.environ["EVENT_PATH"], encoding="utf-8") as fh:
            event = json.load(fh)
    messages = {"issue": os.environ.get("ISSUE_MESSAGE", ""), "pr": os.environ.get("PR_MESSAGE", "")}
    greeted = run(api=http_api(token), repo=repo, event_name=event_name, event=event, messages=messages,
                  now=datetime.now(timezone.utc), lookback_hours=int(os.environ.get("LOOKBACK_HOURS", "3")))
    print(f"greeted: {greeted}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
