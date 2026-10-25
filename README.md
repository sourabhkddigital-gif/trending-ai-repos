# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-25

8 of 10 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br><sub>A coding-agent skill for multi-phase security audits with independently verified, machine-…</sub> | JavaScript | 2,264 | 44,727 | – |
| 2 | [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)<br><sub>OpenShell is the safe, private runtime for autonomous AI agents.</sub> | Rust | 896 | 19,514 | – |
| 3 | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)<br><sub>Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS</sub> | Python | 13 | 3,153 | – |
| 4 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark)<br><sub>Anti-AI-slop design skill for Claude Code, Cursor, and Codex.</sub> | CSS | 455 | 32,224 | – |
| 5 | [luongnv89/claude-howto](https://github.com/luongnv89/claude-howto)<br><sub>A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, wi…</sub> | Python | 392 | 44,607 | `claude-code` `guide` `tutorial` |
| 6 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable)<br><sub>The design language that makes your AI harness better at design.</sub> | Rust | 619 | 86,477 | – |
| 8 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)<br><sub>An open-source AI agent that brings the power of Gemini directly into your terminal.</sub> | TypeScript | 44 | 108,098 | `ai` `ai-agents` `cli` `gemini` |
| 10 | [makecindy/cindy](https://github.com/makecindy/cindy)<br><sub>Consider it done. The open-source AI agent that works out of the box · 想到，就能做到。开源、开箱即用的 AI…</sub> | TypeScript | 477 | 4,138 | `agent` `ai-agent` `ai-assistant` `android` |

### 📊 This week so far · 2026-W43

#### Summary

- **31** distinct AI repos trended over 7 day(s) (last week: 27)
- AI share of all trending slots: **79%** (+1 pts vs last week)
- Dominant language: **Python** (48% of AI repos)
- Rising topics: `cursor` (+4), `pytorch` (+3), `agent` (+2), `ai-agents` (+2), `antigravity` (+2)
- New this week: `cursor`, `pytorch`, `agent`, `claude-code-plugin`, `cursor-rules`, `gemini`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W43-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 15 | 48% | 10 |
| TypeScript | 8 | 26% | 7 |
| Rust | 3 | 10% | 3 |
| JavaScript | 2 | 6% | 1 |
| Unspecified | 1 | 3% | 0 |
| Shell | 1 | 3% | 1 |
| CSS | 1 | 3% | 0 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-topics-dark.png"><img alt="Topic movers" src="charts/2026-W43-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 10 |
| `ai-agents` | 8 |
| `mcp` | 5 |
| `codex` | 5 |
| `skills` | 4 |
| `cursor` | 4 |
| `claude` | 3 |
| `pytorch` | 3 |
| `developer-tools` | 3 |
| `agent-skills` | 3 |
| `antigravity` | 3 |
| `agentic-ai` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 5 | 11,683 | 44,727 |
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 4 | 5,842 | 101,432 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 4 | 3,310 | 141,584 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 3 | 9,949 | 60,828 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 3 | 5,235 | 173,623 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 3 | 3,965 | 219,013 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 3 | 3,643 | 133,052 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 3 | 1,761 | 77,894 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 3 | 1,464 | 12,384 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 3 | 1,333 | 77,303 |

➡️ Last full weekly analysis: [2026-W42](reports/weekly/2026-W42.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 25 day(s) of data · [raw data](data/trending.csv)_
<!-- TRACKER_END -->

## How it works

```
github.com/trending ──► GitHub API (topics, license, created) ──► AI classifier ──► data/trending.csv
                                                                                        │
                                              reports/weekly/YYYY-Www.md + charts ◄─────┘
```

1. **Collect.** Reads the daily [GitHub trending](https://github.com/trending) list (all languages) and records rank, stars, stars gained today, and language for every repository.
2. **Enrich.** Fetches each repository's topics, creation date and license from the GitHub REST API.
3. **Classify.** A repo counts as AI if it carries an AI topic (`llm`, `ai-agents`, `rag`, `mcp`, `computer-vision`, ...) or its name and description match AI keywords. All trending repos are stored, so the AI share of trending can be measured too.
4. **Analyze weekly.** For each finished ISO week (Monday–Sunday):
   - **Languages**: distinct AI repos per primary language, with last week for comparison
   - **Topics**: repos per topic, plus *movers* (biggest gains and drops vs last week) and topics that are new this week. Generic tags like `ai` or `python` are left out, so the movement shows what people are actually building.
   - **Most persistent repos**: AI repos that stayed on the trending list the most days, with stars gained
5. **Fallback.** If GitHub changes the trending page and it can no longer be parsed, the run falls back to the official Search API (new repos with AI topics gaining stars fast) and marks those rows as `search-fallback`, so a day is never empty.

## Data

`data/trending.csv`, one row per repository per day:

| Column | Meaning |
|--------|---------|
| `date`, `rank` | Day (IST) and position on the trending list |
| `repo` | `owner/name` |
| `description`, `language`, `topics`, `license`, `created_at` | Repository metadata |
| `stars`, `forks`, `stars_today` | Totals and stars gained that day |
| `is_ai` | `1` if classified as AI-related |
| `source` | `trending` or `search-fallback` |

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/arielshakaramiro/trending-ai-repos/main/data/trending.csv")
ai = df[df.is_ai == 1]
ai.groupby("language").repo.nunique().sort_values(ascending=False).head(10)
```

## Setup

1. Push this repository to GitHub. No secrets are needed: the workflow uses the built-in `GITHUB_TOKEN` for API calls.
2. **Actions → Daily Trending Snapshot → Run workflow** for the first run.

The first full weekly report appears on the Monday after the first complete week of data. Until then, the live view above shows the week-to-date analysis.

## Run locally

```bash
pip install -r requirements.txt
export GITHUB_TOKEN=ghp_...   # optional, raises the API rate limit
python tracker.py
```

## Customize

`config.json`:

- `ai_topics` / `ai_keywords`: what counts as AI
- `generic_topics`: tags ignored in topic analysis
- `trending_pages`: `[""]` is the all-languages list. Adding e.g. `"python"` also reads that language's list, which finds more repos but skews the language analysis toward the languages you add.
- `since`: `daily`, `weekly` or `monthly`

## License

MIT. Repository data comes from GitHub; each listed project keeps its own license.
