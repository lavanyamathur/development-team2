# Problem 4: Fast & Memory-Efficient Genome Assembly Using AI

_Status as of this doc: Data recreated from the GNNome repository. Setup/reproduction phase in progress._

## Problem Statement

Genome assembly (especially long-read sequencing) is computationally expensive and slow, limiting scalability. Develop a lightweight AI-assisted genome assembly pipeline that reduces computational cost without sacrificing accuracy.

## Our Approach

Shrink GNNome's GNN-based edge-scoring network (full / half / quarter size) and measure the accuracy, efficiency tradeoff as it shrinks, on both a bacterial genome (E. coli DH5α) and a human chromosome (chr19 or chr21), with a specific eye on whether accuracy loss concentrates in repetitive regions or not.

**Pipeline:**

```
real genome → PBSIM3 (simulate long reads) → Raven (build assembly graph)
           → GNNome (score edges/confidence) → search algorithm (follow high-confidence path)
           → assembled genome → QUAST (score against reference)
```

## Genome Sources

- **Bacterial**: E. coli DH5α — NCBI Nucleotide accession CP017100 (single reference genome, single strain, used consistently throughout).
- **Human**: chr19 or chr21, via GNNome's own published test graphs (for direct comparability to their reported numbers).

## Important Points

1. CP017100 (DH5α, via NCBI Nucleotide) as the single reference genome.
2. E. coli has sparse repeat content, so the "does accuracy loss concentrate in repeats?" question may not have enough signal on this genome alone — hence, the plan is to pre-define repeat regions on the DH5α genome before training (rRNA operons + IS elements, or a self-alignment pass), so labeling isn't post-hoc.
3. We'll treat E. coli as a sanity check for this question; treat human chromosome 19/21 as where the claim is actually statistically supported (richer repeat content). *(Important for write-up.)*

## Shrink Model Specifications

Default axis: width (hidden dimension). Depth (number of message-passing layers) held roughly fixed — depth controls how far information propagates across the assembly graph, which matters for long-read path-following. If buffer week allows, we will add one depth-shrunk variant as a bonus point.

### Model Variants

- **Full** — GNNome as published (~220K params), reproduces their reported numbers.
- **Half** — half hidden-dim width, same depth.
- **Quarter** — quarter hidden-dim width, same depth.

## Open Decisions Still Needed

- Exact width-reduction ratios for half/quarter.
- Which LR values go into the per-size sweep, and the sweep protocol (grid vs. small manual search).
- Final call on whether the depth-shrunk variant happens at all, depends on buffer week time.
