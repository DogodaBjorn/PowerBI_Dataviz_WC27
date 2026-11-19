# Contests: one repository, a folder per contest

This root holds no project of its own. Each folder is one contest:

- `powerbi-dataviz-world-champs/`: Power BI Dataviz World Champs, one folder per round, each a whole pbi-atelier
  project. `2027-round1-goodnight-inn/` is entered (16 Nov 2026); the `2026-*` rounds are closed.
- `ai-marketing-kombat/`: AI Marketing Kombat Season 1. One project: toolkit at its root, rounds in `rondes/`.
  Its rules are in its `AGENTS.md`; round 1 (`rondes/2026-10-21-indrive/`) has its own `CLAUDE.md` with that
  case's brand rules.

**Before any work, read the `CLAUDE.md` (or `AGENTS.md`) of the project folder** and treat that folder as the
project root: every path in its documents and scripts is relative to it, and its rules, skills and hooks live in
its `.claude/`. If this session started at this root, say so to Bjorn: the project's skills only load in a session
started in its folder.

`README.md` here says what each folder holds and where it came from. A new contest gets a new folder beside these;
a new Power BI round gets `powerbi-dataviz-world-champs/<year>-round<n>-<name>/`; a new Kombat round gets
`ai-marketing-kombat/rondes/<date>-<name>/`. Never files at this root.
