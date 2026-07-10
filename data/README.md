# Data

Raw genomes, simulated long reads, and assembly graphs are **not committed** to this repository (too large, and often not ours to redistribute).

## Expected local layout

```
data/
├── ecoli-dh5a/
│   ├── CP017100.fasta          # NCBI Nucleotide reference
│   ├── reads/                  # PBSIM3 simulated long reads
│   ├── raven-graph/            # Raven assembly graph output
│   └── repeat-regions.bed      # Pre-defined rRNA operon + IS element regions
├── chr19-or-chr21/
│   ├── reference.fasta
│   └── gnnome-graphs/          # GNNome's published test graphs, used as-is
```

## Sources

- **E. coli DH5α**: NCBI Nucleotide, accession `CP017100`
- **Human chr19/chr21**: GNNome's published test graphs (for direct comparability to their reported numbers)

## Notes

- Repeat regions for DH5α must be pre-defined **before training** (rRNA operons + IS elements, or a self-alignment pass) so labeling isn't post-hoc.
- Add the shared storage link here once the team settles on where large files live (e.g. shared drive, S3 bucket, university cluster path).
