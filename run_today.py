"""Fetch today's GitHub trending repos, save them to a CSV, and print them.

Usage (from this folder):  python run_today.py
Output: trending_today_YYYY-MM-DD.csv in this folder (opens in Excel).
Does not change data/trending.csv or the README.
"""
import csv
import re
import sys
import time
from datetime import date
from pathlib import Path

import tracker as t

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def clean(repo: str, desc: str) -> str:
    # Remove the "Sponsor Star owner / name" button text the trending page leaks into descriptions.
    return re.sub(r"^(?:Sponsor )?Star " + re.escape(repo.replace("/", " / ")) + r" ?", "", desc).strip()


def main() -> int:
    print("Fetching today's trending repositories from github.com/trending ...")
    repos, source = t.fetch_trending()
    if not repos:
        print("Could not reach GitHub. Check your internet connection and try again.")
        return 1
    print(f"  {len(repos)} repos found ({source}). Looking up topics ...")

    rows = []
    for i, r in enumerate(repos, 1):
        r["description"] = clean(r["repo"], r["description"])
        t.enrich(r)
        rows.append({
            "rank": i,
            "repo": r["repo"],
            "url": f"https://github.com/{r['repo']}",
            "description": r["description"],
            "language": r["language"],
            "stars_today": r["stars_today"],
            "total_stars": r["stars"],
            "forks": r["forks"],
            "topics": r["topics"],
            "license": r["license"],
            "is_ai": "yes" if t.is_ai(r) else "no",
        })
        time.sleep(0.3)

    out = Path(__file__).resolve().parent / f"trending_today_{date.today().isoformat()}.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:  # utf-8-sig so Excel shows symbols correctly
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    print()
    print(f"{'#':>2}  {'Repository':<38} {'Language':<11} {'Stars today':>11} {'Total':>9}  AI")
    print("-" * 80)
    for r in rows:
        print(f"{r['rank']:>2}  {r['repo'][:38]:<38} {(r['language'] or '-')[:11]:<11} "
              f"{r['stars_today']:>11,} {r['total_stars']:>9,}  {r['is_ai']}")
    print("-" * 80)
    print(f"{sum(r['is_ai'] == 'yes' for r in rows)} of {len(rows)} are AI-related.")
    print(f"Saved: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
