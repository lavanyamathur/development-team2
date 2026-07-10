# Contributing Guide

This is a small 3-person research group (**[Your Name]**, **Akshat Arora**, **Abhiraj Aarya**). The goal of this guide is to keep everyone's work comparable and easy to find — not to add bureaucracy.

## 1. Branching

- `main` — always stable/reproducible. Don't push broken code directly here.
- Personal/feature branches: `<name>/<short-description>`
  - e.g. `akshat/half-width-gnn`, `abhiraj/quast-wrapper`, `you/pbsim3-config`
- Open a Pull Request into `main` when a piece of work (a script, a variant, an experiment) is ready for others to rely on. Even solo-reviewed PRs are fine — the point is a clean history and a place for notes.

## 2. Commit messages

Keep them short and specific:

```
gnnome: add quarter-width variant config
search: fix path-following tie-break on equal-confidence edges
docs: update open decisions after LR sweep meeting
```

## 3. Where your work goes

| What you're doing | Where it goes |
|---|---|
| Simulating reads (PBSIM3) | `src/simulation/` |
| Building assembly graphs (Raven) | `src/assembly/` |
| GNN model / variant code | `src/gnnome/` |
| Path-following search algorithm | `src/search/` |
| QUAST scoring / evaluation | `src/evaluation/` |
| One-off exploration, plots | `notebooks/` (name with your initials + date, e.g. `aa_repeat_region_plot_0715.ipynb`) |
| Run outputs, metrics, QUAST reports | `results/<genome>/<variant>/` (e.g. `results/ecoli-dh5a/half/`) |
| Model/sweep configs | `configs/` |

## 4. Experiment logging

Every experiment run (a variant × genome combination) should leave behind, under `results/<genome>/<variant>/`:

- The config used (or a pointer to it in `configs/`)
- QUAST output
- A short `NOTES.md`: what was run, any deviations from the config, and one-line takeaway

This is what makes the "does accuracy loss concentrate in repeats?" comparison possible later — we need the three variants (full/half/quarter) × two genomes (E. coli, chr19/21) to be recorded consistently.

## 5. Open decisions

Anything listed under "Open Decisions" in the README should be tracked as a **GitHub Issue** so discussion has a paper trail instead of getting lost in chat. Close the issue with a comment summarizing the final call once decided.

## 6. Data & large files

Raw genomes, simulated reads, and assembly graphs are **not committed** to the repo (see `data/README.md`). Use the shared drive/storage link (add it there once set up) and reference paths in configs.

## 7. Pull request checklist

- [ ] Code runs / experiment reproduces without hardcoded local paths
- [ ] Results (if any) logged under `results/`
- [ ] README/docs updated if this changes the pipeline or open decisions
- [ ] Linked to relevant Issue, if applicable
