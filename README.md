# Fast & Memory-Efficient Genome Assembly Using AI

**Problem 4 — Genome Assembly Research Group**

Team: **Lavanya Mathur**, **Akshat Arora**, **Abhiraj Aarya**

Status: 🔧 Data recreated from the GNNome repository. Setup/reproduction phase in progress.

---

## Problem Statement

Genome assembly — especially from long-read sequencing — is computationally expensive and slow, which limits scalability. This project develops a **lightweight, AI-assisted genome assembly pipeline** that reduces computational cost without sacrificing accuracy.

## Our Approach

We shrink [GNNome's](https://github.com/lvrcek/GNNome) GNN-based edge-scoring network (**full / half / quarter** size) and measure the accuracy–efficiency tradeoff as it shrinks, with fedrann approach in consideration. We test on:

- A **bacterial genome** — *E. coli* DH5α
- A **human chromosome** — chr19 or chr21

with a specific eye on whether accuracy loss concentrates in **repetitive regions** or is spread evenly.

### Pipeline

```
real genome → PBSIM3 (simulate long reads) → Raven (build assembly graph)
           → GNNome (score edges/confidence) → search algorithm (follow high-confidence path)
           → assembled genome → QUAST (score against reference)
```

## Genome Sources

| Genome | Source | Notes |
|---|---|---|
| Bacterial | NCBI Nucleotide accession **CP017100** (*E. coli* DH5α) | Single reference genome, single strain, used consistently throughout |
| Human | GNNome's own published test graphs (chr19 / chr21) | Used for direct comparability to GNNome's reported numbers |

## Key Research Notes

1. **CP017100** (DH5α, via NCBI Nucleotide) is our single reference genome for the bacterial arm.
2. *E. coli* has sparse repeat content, so the "does accuracy loss concentrate in repeats?" question may not have enough signal on this genome alone. Plan: **pre-define repeat regions on the DH5α genome before training** (rRNA operons + IS elements, or a self-alignment pass), so labeling isn't post-hoc.
3. *E. coli* is treated as a **sanity check** for the repeat-concentration question. **Human chr19/chr21** is where the claim is actually meant to be statistically supported (richer repeat content). *(Important for the write-up.)*

## Model Variants (shrinking axis: width)

Depth (number of message-passing layers) is held roughly fixed — depth controls how far information propagates across the assembly graph, which matters for long-read path-following.

| Variant | Description |
|---|---|
| **Full** | GNNome as published (~220K params); reproduces their reported numbers |
| **Half** | Half hidden-dim width, same depth |
| **Quarter** | Quarter hidden-dim width, same depth |

If the buffer week allows, a **depth-shrunk variant** will be added as a bonus.

### Open Decisions (still being finalized — see [Issues](../../issues))

- [ ] Exact width-reduction ratios for half/quarter
- [ ] Which LR values go into the per-size sweep, and the sweep protocol (grid vs. small manual search)
- [ ] Final call on whether the depth-shrunk variant happens at all (depends on buffer week time)

---

## Repository Structure

```
.
├── docs/               # Full spec, design notes, write-up drafts
├── data/               # Genome references, PBSIM3 reads, assembly graphs (not committed — see data/README.md)
├── src/
│   ├── simulation/     # PBSIM3 wrappers — long-read simulation
│   ├── assembly/       # Raven wrappers — assembly graph construction
│   ├── gnnome/         # GNN edge-scoring model + full/half/quarter variants
│   ├── search/         # High-confidence path-following search algorithm
│   └── evaluation/     # QUAST wrappers — scoring against reference
├── notebooks/          # Exploratory analysis, plots
├── results/            # Metrics, logs, QUAST reports per variant/genome
├── configs/            # Model variant configs, LR sweep configs
└── requirements.txt
```

## Getting Started

```bash
git clone https://github.com/<your-username>/development-team2.git
cd development-team2
pip install -r requirements.txt
```

See `docs/research-spec.md` for the full problem spec and `CONTRIBUTING.md` for how to add your work.

## Contributing

All team members: please read [CONTRIBUTING.md](CONTRIBUTING.md) before pushing — it covers branch naming, commit style, and where experiment results/configs should live so everything stays comparable across variants and genomes.

## References

- GNNome: https://github.com/lvrcek/GNNome
- PBSIM3
- Raven assembler
- QUAST
