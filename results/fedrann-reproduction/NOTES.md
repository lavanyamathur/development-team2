# FEDRANN Reproduction — C. elegans (SRR10028111)

## What was run
Attempted to reproduce results from the FEDRANN paper (GigaScience 2026) using the
paper's own C1O dataset: *C. elegans* ONT reads, SRA accession SRR10028111,
aligned against the WBcel235 reference genome.

Due to local hardware constraints (12GB RAM via WSL2), the full 790K-read dataset
could not be run. Instead, read-count subsets (first N reads from the FASTQ) were
tested at 20,000 and 50,000 reads.

## Files in this folder
- `overlaps_20k_k15.tsv.gz` — Fedrann output, 20K reads, k=15, kmer-sample-fraction=0.01,
  embedding-dimension=100, nndescent-n-trees=50, nndescent-n-neighbors=20
- `overlaps_20k_k13.tsv.gz` — same as above but k=13 (paper's recommended k-mer size for ONT)
- `overlaps_50k.tsv.gz` — Fedrann output, 50K reads, k=15, kmer-sample-fraction=0.005,
  embedding-dimension=50, nndescent-n-trees=30 (reduced further to fit memory)
- `compare_to_truth*.py` — scripts that align reads to reference via minimap2,
  build a ground-truth overlap graph from alignment intervals, and compute error
  rate/recall against Fedrann's predicted overlaps

## Deviations from paper's methodology
- Paper used full whole-genome datasets (790K+ reads for C1O); we used small
  read-count subsets due to memory constraints
- Had to patch a hardcoded `hash_size = "10G"` in Fedrann's `count_kmers.py`
  (Jellyfish call) down to `1G` to avoid OOM kills on our hardware
- Truth graph built via a simplified script (pysam-based), not
