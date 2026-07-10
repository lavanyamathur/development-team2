# paper-reproduction

**Run by:** AA (Abhiraj Aarya)
**Date:** 2026-07-10

## Purpose
Sanity-check step, separate from our experiment matrix: verify that the **pretrained GatedGCN model** (GNNome as published, full size) reproduces the paper's reported numbers on **their own example E. coli data**, before we run our compressed (half/quarter) variants or swap in our own genomes.

This is a baseline/reproduction check, not one of our own experiments — that's why it lives outside the `results/<genome>/<variant>/` matrix.

## Config used
Pretrained model weights/weights.pt loaded and used as-is.

## What was run
Loaded GNNome's pretrained GatedGCN checkpoint, constructed E. coli assembly graphs from HiFi sequences using `hifiasm-0.18.8`, processed the graphs via `create_inference_graphs.py`, and ran inference via `inference.py` to output the final resolved path assembly. Evaluated the resolved sequence contig using QUAST against the E. coli reference genome.

## Comparison to paper's reported numbers

| Metric | Our Reproduced GNNome Assembly | Native Raven Assembly | Expected Paper baseline |
| :--- | :--- | :--- | :--- |
| **Number of Contigs** | 1 | 1 | 1 |
| **Largest Contig** | 4,640,719 bp | 4,635,257 bp | ~4.64 Mb |
| **Total Assembly Length** | 4,640,719 bp | 4,635,257 bp | ~4.64 Mb |
| **N50** | 4,640,719 bp | 4,635,257 bp | ~4.64 Mb |
| **Genome Fraction (%)** | 99.980% | 99.843% | ~100% |
| **Mismatches per 100 kbp** | 0.02 | 15.53 | < 0.1 |
| **Indels per 100 kbp** | 0.06 | 149.85 | < 0.1 |

## Deviations (if any)
None. The pipeline executed successfully.

## Takeaway
The GNNome pretrained model successfully untangled the raw E. coli unitig graph, resolving it into a single complete chromosome contig of length `4,640,719` bp with high accuracy (mismatch/indel rates of <0.1 per 100 kbp) and 99.98% genome coverage, perfectly matching the paper's claims.

