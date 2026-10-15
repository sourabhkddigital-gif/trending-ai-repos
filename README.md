# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-15

7 of 12 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br><sub>Reverse engineer anything with agents, from app behavior down to native binaries.</sub> | TypeScript | 41,034 | 245,056 | `agent-skills` `ai-agents` `binary-analysis` `claude-code` |
| 2 | [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)<br><sub>VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice …</sub> | Python | 3,538 | 66,585 | `ai` `audiobook` `cuda` `dubbing` |
| 3 | [mksglu/context-mode](https://github.com/mksglu/context-mode)<br><sub>Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), p…</sub> | TypeScript | 947 | 29,201 | `antigravity` `claude` `claude-code` `claude-code-hooks` |
| 5 | [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br><sub>Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by 2…</sub> | Python | 163 | 49,438 | `agent-skills` `ai-scientist` `bioinformatics` `chemoinformatics` |
| 6 | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)<br><sub>"CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/</sub> | Python | 103 | 52,571 | – |
| 7 | [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi)<br><sub>Independent Auditing of AI Agents. Run by human or the agent itself, to answer the most cr…</sub> | Python | 2,109 | 27,543 | `agent-evaluation` `ai` `ai-alignment` `ai-evaluation` |
| 8 | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)<br><sub>Fully autonomous AI Agents system capable of performing complex penetration testing tasks</sub> | Go | 1,025 | 29,609 | `ai-agents` `ai-security-tool` `anthropic` `autonomous-agents` |

### 📊 This week so far · 2026-W42

#### Summary

- **15** distinct AI repos trended over 4 day(s) (last week: 33)
- AI share of all trending slots: **71%** (-3 pts vs last week)
- Dominant language: **Python** (47% of AI repos)
- Rising topics: `self-hosted` (+1)

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W42-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W42-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 7 | 47% | 10 |
| TypeScript | 3 | 20% | 5 |
| Rust | 1 | 7% | 2 |
| HTML | 1 | 7% | 1 |
| Jupyter Notebook | 1 | 7% | 0 |
| C++ | 1 | 7% | 1 |
| Go | 1 | 7% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W42-topics-dark.png"><img alt="Topic movers" src="charts/2026-W42-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `codex` | 3 |
| `agent-skills` | 3 |
| `claude-code` | 3 |
| `mcp` | 3 |
| `ai-agents` | 2 |
| `cli` | 2 |
| `claude` | 2 |
| `self-hosted` | 2 |
| `openai` | 2 |
| `dsh` | 1 |
| `ghidra` | 1 |
| `reverse-engineering` | 1 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [morluto/rea](https://github.com/morluto/rea) | TypeScript | 4 | 166,639 | 245,056 |
| [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 3 | 11,133 | 25,882 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 3 | 4,979 | 54,274 |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 3 | 2,428 | 38,383 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | TypeScript | 3 | 2,162 | 29,201 |
| [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) | Python | 2 | 5,286 | 66,585 |
| [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi) | Python | 1 | 2,109 | 27,543 |
| [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Go | 1 | 1,025 | 29,609 |
| [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) | Python | 1 | 626 | 59,217 |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | Python | 1 | 315 | 104,537 |

➡️ Last full weekly analysis: [2026-W41](reports/weekly/2026-W41.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 15 day(s) of data · [raw data](data/trending.csv)_
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
