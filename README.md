# Contests

Every contest Björn Kats (DoGoDa) enters, in one repository: one folder per contest, the rounds inside it.
Nothing contest-related lives anywhere else on the machine (`E:\Contests`).

| Folder | Contest | What it holds | State |
|---|---|---|---|
| [`powerbi-dataviz-world-champs/`](powerbi-dataviz-world-champs/) | Power BI Dataviz World Champs | One folder per round: 2027 Round 1 "Goodnight Inn - Room to Invest", and Barcelona 2026 Rounds 1 to 3. Each round folder is a whole pbi-atelier project | 2027 Round 1 entered 16 Nov 2026; Round 2 runs 25 Nov to 9 Dec 2026 |
| [`ai-marketing-kombat/`](ai-marketing-kombat/) | AI Marketing Kombat, Season 1 (track Performance & Analytics) | The toolkit (skills, knowledge base, calculators, panel) and the rounds in `rondes/`: round 1 inDrive Nigeria, round 2 AxisX | Rounds 1 and 2 delivered in Oct 2026; the final (Fabergé) ahead |

## How to work here

Each contest folder, and for the Power BI contest each round folder, is a project of its own with its own
`CLAUDE.md` or `AGENTS.md`, skills and `.gitignore`. **Open that folder as the working directory**: Claude Code
loads skills and rules from the folder it starts in, and every path in a project's documents and scripts is
relative to its own folder.

| To work on | Open |
|---|---|
| A Power BI World Champs round | `powerbi-dataviz-world-champs/<year>-round<n>-<name>/` |
| An AI Marketing Kombat round | `ai-marketing-kombat/` (the round's files go in `rondes/<date>-<name>/`) |
| A new contest | a new folder here, `<contest-name>/`, never files at this root |

## Where it came from

| Folder | Was | When |
|---|---|---|
| `powerbi-dataviz-world-champs/` | the repository `PowerBI_Dataviz_WC27` itself (its index is now that folder's `README.md`), which on 18 Nov 2026 had taken in `hp-world-champs`, `wc-round-3` and `world-champs-r2` | 19 Nov 2026, moved one level down |
| `ai-marketing-kombat/` | repository `PerformanceOps` (`E:\PerformanceOps`), branch `master`, 26 commits | 19 Nov 2026, merged with its history |
| `ai-marketing-kombat/rondes/2026-10-21-indrive/` | repository `indrive-kombat` (`E:\InDrive Kombat`), branch `main`, 2 commits | 19 Nov 2026, merged with its history |

The older repositories still exist on GitHub (`hp-world-champs`, `wc-round-3`, `world-champs-r2`, `PerformanceOps`,
`indrive-kombat`); the work no longer lives there. GitHub forwards the old address of this repository
(`DogodaBjorn/PowerBI_Dataviz_WC27`) to `DogodaBjorn/contests`.

---
Part of the workspace of Björn Kats (DoGoDa). Map, status of all repos and agent briefings:
[DogodaBjorn/workspace](https://github.com/DogodaBjorn/workspace) (private).
