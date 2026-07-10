# Results

Organize results by genome, then variant:

```
results/
├── paper-reproduction/  # Sanity check: pretrained GNNome reproduces paper's claims on their own E. coli example data
├── ecoli-dh5a/
│   ├── full/
│   │   ├── quast_report/
│   │   └── NOTES.md
│   ├── half/
│   └── quarter/
└── chr19-or-chr21/
    ├── full/
    ├── half/
    └── quarter/
```

`paper-reproduction/` sits outside the `<genome>/<variant>` matrix on purpose — it's a one-off baseline check (does the published pretrained model reproduce the paper's reported numbers?), not one of our own experiments, so mixing it into the matrix would be misleading.

Each `NOTES.md` should briefly note: what was run, the config used, any deviations, and a one-line takeaway. See `CONTRIBUTING.md` section 4 for details.
