# Trending AI Repos Tracker

A daily record of which AI repositories are trending on GitHub, with a weekly analysis of **which topics are rising** and **which languages dominate**.

Every morning a GitHub Actions workflow reads the GitHub trending page, looks up each repository's topics, flags the AI-related ones, and appends the day to a CSV. Every Monday the previous week is analyzed and saved as a report with charts. The section below refreshes daily with today's list and the week so far.

## Live view

<!-- TRACKER_START -->
### 🔥 AI repos trending today · 2026-10-10

10 of 11 trending repositories are AI-related.

| # | Repo | Language | ⭐ today | ⭐ total | Topics |
|--:|---|---|--:|--:|---|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br><sub>Reverse engineer anything with agents, from app behavior down to native binaries.</sub> | TypeScript | 14,927 | 48,196 | `agent-skills` `ai-agents` `binary-analysis` `claude-code` |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills)<br><sub>Skills for Real Engineers. Straight from my .agents directory.</sub> | Shell | 1,687 | 282,829 | – |
| 4 | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)<br><sub>Editorial diagram design for Claude Code, Codex, GitHub Copilot, Factory Droid, and Pi. 42…</sub> | HTML | 1,739 | 47,960 | `agent-skills` `claude-code` `codex` `data-visualization` |
| 5 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review)<br><sub>Secure, fast, efficient, battle-tested at Alibaba's scale. Hybrid architecture code review…</sub> | Go | 326 | 45,301 | `agent` `agent-skills` `code-review` `code-review-assistant` |
| 6 | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)<br><sub>Open source repository of plugins primarily intended for knowledge workers to use in Claud…</sub> | Python | 709 | 28,303 | – |
| 7 | [BerriAI/litellm](https://github.com/BerriAI/litellm)<br><sub>The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (o…</sub> | Python | 95 | 60,695 | `ai-gateway` `anthropic` `azure-openai` `bedrock` |
| 8 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)<br><sub>Production-grade engineering skills for AI coding agents.</sub> | JavaScript | 436 | 104,034 | `agent-skills` `antigravity` `claude-code` `codex` |
| 9 | [storytold/artcraft](https://github.com/storytold/artcraft)<br><sub>ArtCraft is an intentional crafting engine for artists, designers, and filmmakers</sub> | Rust | 3,752 | 11,688 | `3d-graphics` `ai` `aivideo` `filmmaking` |
| 10 | [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map)<br><sub>[ECCV 2026 Best Paper Award Candidate] LingBot-Map: Geometric Context Transformer for Stre…</sub> | Python | 110 | 17,736 | – |
| 11 | [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)<br><sub>SwiftUI agent skill for Claude Code, Codex, and other AI tools.</sub> | – | 65 | 5,479 | – |

### 📊 This week so far · 2026-W41

#### Summary

- **27** distinct AI repos trended over 6 day(s) (last week: 28)
- AI share of all trending slots: **72%** (-5 pts vs last week)
- No single dominant language: JavaScript, Python tied at 7 repo(s) each
- Rising topics: `agent` (+3), `agent-skills` (+2), `claude-code-plugin` (+2), `claude-skills` (+2), `code-review` (+2)
- New this week: `agent`, `openai`, `code-review`, `macos`

#### Languages

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-languages-dark.png"><img alt="Languages of trending AI repos" src="charts/2026-W41-languages.png"></picture>

| Language | Repos | Share | Last week |
|---|--:|--:|--:|
| JavaScript | 7 | 26% | 5 |
| Python | 7 | 26% | 7 |
| TypeScript | 4 | 15% | 9 |
| Shell | 2 | 7% | 2 |
| Rust | 2 | 7% | 2 |
| C | 1 | 4% | 1 |
| HTML | 1 | 4% | 0 |
| Swift | 1 | 4% | 0 |
| Go | 1 | 4% | 1 |
| Unspecified | 1 | 4% | 0 |

#### Topics

<picture><source media="(prefers-color-scheme: dark)" srcset="charts/2026-W41-topics-dark.png"><img alt="Topic movers" src="charts/2026-W41-topics.png"></picture>

| Topic | Repos this week |
|---|--:|
| `claude-code` | 8 |
| `codex` | 6 |
| `agent-skills` | 6 |
| `claude` | 5 |
| `developer-tools` | 4 |
| `ai-agents` | 4 |
| `claude-code-plugin` | 4 |
| `cursor` | 3 |
| `mcp` | 3 |
| `cli` | 3 |
| `agent` | 3 |
| `anthropic` | 3 |

#### Most persistent AI repos

| Repo | Language | Days trending | Stars gained | Total stars |
|---|---|--:|--:|--:|
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | TypeScript | 5 | 2,944 | 98,540 |
| [morluto/rea](https://github.com/morluto/rea) | TypeScript | 4 | 30,276 | 48,196 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 4 | 5,753 | 282,829 |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 4 | 3,952 | 47,960 |
| [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym) | JavaScript | 3 | 4,345 | 6,998 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | JavaScript | 3 | 1,449 | 104,034 |
| [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) | Python | 3 | 1,139 | 18,104 |
| [storytold/artcraft](https://github.com/storytold/artcraft) | Rust | 2 | 5,855 | 11,688 |
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | Python | 2 | 2,135 | 92,214 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 2 | 1,787 | 77,863 |

➡️ Last full weekly analysis: [2026-W40](reports/weekly/2026-W40.md) · [all reports](reports/weekly)

_Tracking since 2026-10-01 · 10 day(s) of data · [raw data](data/trending.csv)_
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
