# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-11

11 of 13 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br><sub>Reverse engineer anything with agents, from app behavior down to native binaries.</sub> | TypeScript | 25,793 | 74,328 | `agent-skills` `ai-agents` `binary-analysis` `claude-code` |
| 3 | [storytold/artcraft](https://github.com/storytold/artcraft)<br><sub>ArtCraft is an intentional crafting engine for artists, designers, and filmmakers</sub> | Rust | 3,222 | 14,643 | `3d-graphics` `ai` `aivideo` `filmmaking` |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)<br><sub>Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, an…</sub> | HTML | 1,190 | 49,024 | `agent-skills` `claude-code` `codex` `data-visualization` |
| 5 | [mksglu/context-mode](https://github.com/mksglu/context-mode)<br><sub>Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), p…</sub> | TypeScript | 178 | 26,346 | `antigravity` `claude` `claude-code` `claude-code-hooks` |
| 6 | [mattpocock/skills](https://github.com/mattpocock/skills)<br><sub>Skills for Real Engineers. Straight from my .agents directory.</sub> | Shell | 1,736 | 284,592 | – |
| 8 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)<br><sub>An Open Source Machine Learning Framework for Everyone</sub> | C++ | 26 | 200,739 | `deep-learning` `deep-neural-networks` `distributed` `machine-learning` |
| 9 | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)<br><sub>AI turns documents or topics into real, native PowerPoint decks—with native shapes, transi…</sub> | Python | 461 | 59,531 | `ai-agent` `aippt` `office` `powerpoint` |
| 10 | [pytorch/pytorch](https://github.com/pytorch/pytorch)<br><sub>Tensors and Dynamic neural networks in Python with strong GPU acceleration</sub> | Python | 84 | 104,154 | `autograd` `deep-learning` `gpu` `machine-learning` |
| 11 | [huggingface/transformers](https://github.com/huggingface/transformers)<br><sub>🤗 Transformers: the model-definition framework for state-of-the-art machine learning model…</sub> | Python | 96 | 167,287 | `audio` `deep-learning` `deepseek` `gemma` |
| 12 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)<br><sub>Open source repository of plugins primarily intended for knowledge workers to use in Claud…</sub> | Python | 625 | 28,845 | – |
| 13 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)<br><sub>A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's ob…</sub> | – | 278 | 218,326 | – |

### 📊 This week so far · 2026-W41

#### Summary

- **33** distinct AI repos trended over 7 day(s) (last week: 28)
- AI share of all trending slots: **74%** (-3 pts vs last week)
- Dominant language: **Python** (30% of AI repos)
- Rising topics: `agent` (+3), `codex` (+3), `agent-skills` (+2), `ai-agent` (+2), `claude-code-plugin` (+2)
- New this week: `agent`, `openai`, `code-review`, `macos`, `neural-network`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W41-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| Python | 10 | 30% | 7 |
| JavaScript | 7 | 21% | 5 |
| TypeScript | 5 | 15% | 9 |
| Shell | 2 | 6% | 2 |
| Rust | 2 | 6% | 2 |
| Unspecified | 2 | 6% | 0 |
| C | 1 | 3% | 1 |
| HTML | 1 | 3% | 0 |
| Swift | 1 | 3% | 0 |
| Go | 1 | 3% | 1 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-topics-dark.png"><img alt="Topic movers" src="charts/2026-W41-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 9 |
| `codex` | 7 |
| `claude` | 6 |
| `agent-skills` | 6 |
| `ai-agents` | 4 |
| `claude-code-plugin` | 4 |
| `developer-tools` | 4 |
| `mcp` | 4 |
| `ai-agent` | 3 |
| `cursor` | 3 |
| `cli` | 3 |
| `agent` | 3 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [morluto/rea](https://github.com/morluto/rea) | TypeScript | 5 | 56,069 | 74,328 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 5 | 7,489 | 284,592 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 5 | 5,142 | 49,024 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 5 | 2,944 | 98,540 |
| [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 3 | 9,077 | 14,643 |
| [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | JavaScript | 3 | 4,345 | 6,998 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Python | 3 | 1,726 | 28,845 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 3 | 1,449 | 104,034 |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Python | 3 | 1,139 | 18,104 |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 2 | 2,135 | 92,214 |

➡️ Last full weekly analysis: [2026-W40](reports/weekly/2026-W40.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 11 day(s) of data · [raw data](data/trending.csv)_
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
