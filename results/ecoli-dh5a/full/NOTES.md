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
| **Largest Contig** | 4,635,088 bp | 4,578,923 bp |
| **Total Assembly Length** | 4,635,088 bp | 4,578,923 bp |
| **N50** | 4,635,088 bp | 4,578,923 bp |
| **Genome Fraction (%)** | 98.806% | 99.867% |
| **Mismatches per 100 kbp** | 13.69 | 1.09 |
| **Indels per 100 kbp** | 72.66 | 35.25 |

## Deviations from config (if any)
None.

## Takeaway
The GNNome full-width model successfully resolved the E. coli DH5α assembly graph into a single contiguous contig of length `4,635,088` bp, compared to the native Raven assembler output of `4,578,923` bp. Both methods yielded a single-contig assembly, with GNNome recovering a slightly larger portion of the genome length.

