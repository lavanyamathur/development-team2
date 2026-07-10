# ecoli-dh5a — full

**Run by:** AA (Abhiraj Aarya)
**Date:** 2026-07-10

## Config used
Pretrained GNNome model weights used as-is.

## What was run
Ran GNNome full-width model pipeline starting from simulated PBSIM3 reads and the Raven-constructed assembly graph. Scored edges using the pretrained GatedGCN model and untangled the path. Evaluated the final assembly contig against the E. coli DH5α reference genome (NCBI accession `CP017100`) using QUAST.

## Comparison Table
| Metric | GNNome (full) | Native Raven |
| :--- | :--- | :--- |
| **Number of Contigs** | 1 | 1 |
| **Largest Contig** | 4,581,340 bp | 4,581,274 bp |
| **Total Assembly Length** | 4,581,340 bp | 4,581,274 bp |
| **N50** | 4,581,340 bp | 4,581,274 bp |
| **Genome Fraction (%)** | 99.930% | 99.930% |
| **Mismatches per 100 kbp** | 8.60 | 15.45 |
| **Indels per 100 kbp** | 94.45 | 160.98 |

## Deviations from config (if any)
None.

## Takeaway
The GNNome full-width model successfully assembled the E. coli DH5α genome into a single contig of length `4,581,340` bp, significantly reducing mismatch (8.60 vs 15.45) and indel (94.45 vs 160.98) rates compared to the native Raven assembler while preserving contiguity.

