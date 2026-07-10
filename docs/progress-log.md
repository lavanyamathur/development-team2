# Progress Log

A running, dated log of what's been done, decided, or found. Plain language, not code — the goal is that anyone (or future-you, writing up the report) can skim this and reconstruct the project's timeline without digging through commit history.

**How to use this:** add a new dated entry at the top whenever something notable happens — a decision gets made, an experiment finishes, a blocker comes up. Sign off with your initials.

---

## 2026-07-10 — Repo setup (LM)

- Set up the GitHub repo (`development-team2`, private) with the full pipeline scaffold: `src/simulation`, `src/assembly`, `src/gnnome`, `src/search`, `src/evaluation`, plus `configs/`, `docs/`, `results/`, `notebooks/`.
- Added `CONTRIBUTING.md` covering branching, where work goes, and experiment logging convention (`results/<genome>/<variant>/NOTES.md`).
- Ported the original problem spec into `docs/research-spec.md`.
- Akshat Arora and Abhiraj Aarya added as collaborators.

### Open decisions carried over from the spec (unresolved as of this entry)
- Exact width-reduction ratios for half/quarter variants.
- LR values for the per-size sweep, and sweep protocol (grid vs. small manual search).
- Whether the depth-shrunk bonus variant happens at all (depends on buffer week time).

### Status
- Data recreated from the GNNome repository.
- Setup/reproduction phase in progress — no experiments run yet.
