# paper-reproduction

**Run by:** _(initials)_
**Date:** _(yyyy-mm-dd)_

## Purpose
Sanity-check step, separate from our experiment matrix: verify that the **pretrained GatedGCN model** (GNNome as published, full size) reproduces the paper's reported numbers on **their own example E. coli data**, before we run our compressed (half/quarter) variants or swap in our own genomes.

This is a baseline/reproduction check, not one of our own experiments — that's why it lives outside the `results/<genome>/<variant>/` matrix.

## Config used
_(link to configs/model_variants.yaml "full" entry, or note if the pretrained checkpoint was used as-is)_

## What was run
_(e.g. "Loaded GNNome's pretrained GatedGCN checkpoint, ran on GNNome's published E. coli example graph, compared output metrics against paper's reported numbers")_

## Comparison to paper's reported numbers
_(table or brief note: our reproduced metric vs. paper's reported metric)_

## Deviations (if any)


## Takeaway
_(one line — did it reproduce successfully? any discrepancies worth flagging before moving to our own variants?)_
