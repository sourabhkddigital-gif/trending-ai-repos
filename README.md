# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-22

10 of 11 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br><sub>A coding-agent skill for multi-phase security audits with independently verified, machine-…</sub> | JavaScript | 2,012 | 36,708 | – |
| 2 | [vllm-project/vllm](https://github.com/vllm-project/vllm)<br><sub>A high-throughput and memory-efficient inference and serving engine for LLMs</sub> | Python | 441 | 94,915 | `amd` `blackwell` `cuda` `deepseek` |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br><sub>Orca is the place for working with a fleet of agents (e.g. Grok Bot, Claude Code). Run any…</sub> | TypeScript | 1,541 | 101,432 | `ade` `agent-ide` `ai-agents` `automation` |
| 4 | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)<br><sub>Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer to…</sub> | Python | 474 | 77,303 | `agent` `ai` `anthropic` `claude-code` |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br><sub>Makes your AI agent think like the laziest senior dev in the room. The best code is the co…</sub> | JavaScript | 2,079 | 171,800 | `agent-skills` `ai-agents` `claude` `claude-code` |
| 6 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)<br><sub>The most powerful and modular diffusion model GUI, api and backend with a graph/nodes inte…</sub> | Python | 939 | 141,584 | `ai` `comfy` `comfyui` `python` |
| 7 | [supabase/supabase](https://github.com/supabase/supabase)<br><sub>The Postgres development platform. Supabase gives you a dedicated Postgres database to bui…</sub> | TypeScript | 504 | 113,052 | `ai` `alternative` `auth` `database` |
| 8 | [twentyhq/twenty](https://github.com/twentyhq/twenty)<br><sub>The open alternative to Salesforce, designed for AI.</sub> | TypeScript | 112 | 59,221 | `crm` `crm-system` `customer` `good-first-issue` |
| 10 | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)<br><sub>Solution for long term memory for agent coding CLIs and to facilitate handoff between diff…</sub> | Rust | 286 | 12,384 | – |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br><sub>Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowled…</sub> | Python | 1,433 | 131,751 | `ai-agents` `antigravity` `ast` `claude-code` |

### 📊 This week so far · 2026-W43

#### Summary

- **22** distinct AI repos trended over 4 day(s) (last week: 27)
- AI share of all trending slots: **84%** (+5 pts vs last week)
- Dominant language: **Python** (50% of AI repos)
- Rising topics: `cursor` (+4), `antigravity` (+2), `claude-code-plugin` (+2), `cursor-rules` (+2), `postgresql` (+2)
- New this week: `cursor`, `pytorch`, `claude-code-plugin`, `cursor-rules`, `postgresql`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W43-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 11 | 50% | 10 |
| TypeScript | 6 | 27% | 7 |
| JavaScript | 2 | 9% | 1 |
| Rust | 1 | 5% | 3 |
| Unspecified | 1 | 5% | 0 |
| Shell | 1 | 5% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W43-topics-dark.png"><img alt="Topic movers" src="charts/2026-W43-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 8 |
| `ai-agents` | 7 |
| `mcp` | 5 |
| `codex` | 4 |
| `cursor` | 4 |
| `skills` | 3 |
| `claude` | 3 |
| `agent-skills` | 3 |
| `developer-tools` | 3 |
| `antigravity` | 3 |
| `multi-agent` | 2 |
| `agentic-ai` | 2 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [stablyai/orca](https://github.com/stablyai/orca) | TypeScript | 4 | 5,842 | 101,432 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | Python | 4 | 3,310 | 141,584 |
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | Python | 3 | 9,949 | 60,828 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | TypeScript | 3 | 3,965 | 219,013 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | TypeScript | 3 | 1,761 | 77,894 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | Rust | 3 | 1,464 | 12,384 |
| [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Python | 3 | 1,333 | 77,303 |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 2 | 3,724 | 36,708 |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | JavaScript | 2 | 3,287 | 171,800 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 2 | 2,235 | 131,751 |

➡️ Last full weekly analysis: [2026-W42](reports/weekly/2026-W42.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 22 day(s) of data · [raw data](data/trending.csv)_
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
