# GNNome Baseline Data Recreation Proof

This document provides complete proof and documentation of the GNNome baseline data recreation, including the exact commands, git metadata, environment packages, raw execution logs, and output file locations for both the **E. coli K12 example (paper reproduction)** and the **E. coli DH5α full baseline** assemblies.

---

## 1. Git Repository Information

- **Repository Cloned:** `https://github.com/abhiraj-arya2006/GNNome-v2.git`
- **Upstream Source:** `https://github.com/lbcb-sci/GNNome.git`
- **Commit Hash:** `418c7d30e9bd2e4dcf521deebf42a5ba07836c9f`
- **Date of Recreation Logged:** 2026-07-10
- **User/Runner:** Abhiraj Arya (AA)

---

## 2. Exact Step-by-Step Commands Run (In Order)

### System & Conda Environment Setup
```bash
# Update packages and install build requirements
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential cmake zlib1g-dev git wget curl

# Download and install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Clone GNNome repository and setup Conda environment
git clone https://github.com/abhiraj-arya2006/GNNome-v2.git GNNome
cd GNNome
conda create -n gnnome python=3.8 pip -y
conda activate gnnome

# Install CMake and Zlib within the environment
conda install -y cmake
conda install -y zlib
conda install -y cudatoolkit=11.0

# Install dependencies and tools
pip install -r requirements.txt
python install_tools.py
```

### Running K12 Example Baseline (Paper Reproduction)
```bash
# Step 1: Construct the assembly graph using Hifiasm
mkdir -p example/hifiasm/output
./vendor/hifiasm-0.18.8/hifiasm --prt-raw -o example/hifiasm/output/ecoli_asm -t 8 -l0 example/ecoli.fasta.gz

# Step 2: Prepare graphs for GNNome inference (Generates processed DGL graphs)
python create_inference_graphs.py --reads example/ecoli.fasta.gz --gfa example/hifiasm/output/ecoli_asm.bp.raw.r_utg.gfa --asm hifiasm --out example

# Step 3: Run edge scoring and path untangling inference
python inference.py --data example --asm hifiasm --out example/hifiasm

# Step 4: Run QUAST evaluation
quast -r Ecoli_K12_ref.fasta example/hifiasm/assembly/0_assembly.fasta raven_assembly.fasta -o quast_final/
```

### Running E. coli DH5α Full Baseline
```bash
# Step 1: Simulate DH5α reads using PBSIM3
./vendor/pbsim3/src/pbsim --strategy wgs --method qshmm --qshmm ./vendor/pbsim3/data/QSHMM-RSII.model --depth 20 --genome data/dh5alpha/CP017100.fasta --prefix data/dh5alpha/simulated

# Step 2: Construct assembly graph using Raven
./vendor/raven-1.8.1/build/bin/raven -t 8 -p0 data/dh5alpha/dh5alpha_reads.fastq.gz > data/CP017100_assembly.fasta

# Step 3: Run QUAST scoring for both GNNome resolved path and Raven baseline
quast data/raven/assembly/0_assembly.fasta -r data/CP017100.fasta -o data/raven/quast_results
quast data/CP017100_assembly.fasta -r data/CP017100.fasta -o data/classical_raven_quast_results
```

---

## 3. Environment & Package Info

### Python Version
- **Python Version:** 3.8.20
- **Pip Version:** 24.2

### Pip Package List (`pip list`)
```text
Package                       Version
----------------------------- ------------
biopython                     1.79
cffi                          1.15.1
dgl-cu111                     0.8.1
dglgo                         0.0.1
edlib                         1.3.9
matplotlib                    3.4.2
networkx                      2.5.1
numpy                         1.20.3
Pillow                        8.2.0
quast                         5.3.0
scikit-learn                  0.24.2
scipy                         1.6.3
torch                         1.9.0+cu111
torchaudio                    0.9.0
torchvision                   0.10.0+cu111
tqdm                          4.62.2
```

---

## 4. Raw Console Output / Log from the Run
Here is the exact stdout log captured during the K12 example pipeline run:

```text
==================================================
Step 1: Constructing assembly graph with Hifiasm...
==================================================
Reads has been loaded.
Loading ma_hit_ts from disk... 
ma_hit_ts has been read.
Loading ma_hit_ts from disk... 
ma_hit_ts has been read.
[M::ha_assemble::0.096*0.94] ==> loaded corrected reads and overlaps from disk
[M::ha_opt_update_cov_min] updated max_n_chain to 145
Writing raw unitig GFA to disk... 
[M::purge_dups] homozygous read coverage threshold: 28
[M::purge_dups] purge duplication coverage threshold: 35
Writing raw unitig GFA to disk... 
Writing processed unitig GFA to disk... 
[M::adjust_utg_by_primary] primary contig coverage range: [23, infinity]
Writing primary contig GFA to disk... 
Writing alternate contig GFA to disk... 
Inconsistency threshold for low-quality regions in BED files: 70%
[M::main] Version: 0.18.8-r525
[M::main] CMD: ./vendor/hifiasm-0.18.8/hifiasm --prt-raw -o example/hifiasm/output/ecoli_asm -t 8 -l0 example/ecoli.fasta.gz
[M::main] Real time: 0.577 sec; CPU: 0.566 sec; Peak RSS: 0.106 GB

==================================================
Step 2: Processing assembly graphs...
==================================================
Starting to parse assembler output
Starting to loop over GFA
Elapsed time: 0s
Elapsed time: 0s
Calculating similarities...
100%|███████████████████████████████████████████████████████████████████████████| 55496/55496 [00:09<00:00, 5810.38it/s]
Done!
Elapsed time: 10s
Parsed assembler output! Saving files...
Processing of graph done!

==================================================
Step 3: Generating assembly sequence...
==================================================
Number of graphs in the dataset: 1

elapsed time (loading network and data): 0h 0m 0s

==== Processing graph 0 ====
Decoding with model scores...
Loading the scores from:
example/hifiasm/decode/0_predicts.pt

elapsed time (get_scores): 0h 0m 0s
Loading successors...
Loading predecessors...
Loading edges...
Done loading the auxiliary graph data!
Starting to decode with greedy...
num_candidates: 100

Elapsed time (sample edges): 0h 0m 0s

idx_contig: 0, nb_processed_nodes: 0, nb_remaining_nodes: 5120, nb_original_nodes: 5120
0  : src=315      dst=1909     len_walk=388      len_contig=4640719      sumLogProb=-15.961      meanLogProb=-0.04135     meanLogProb_scaled=-1.919e-05  
1  : src=1151     dst=1881     len_walk=387      len_contig=4640716      sumLogProb=-15.923      meanLogProb=-0.04136     meanLogProb_scaled=-1.92e-05   
...
Chosen walk with index: 0
len_walk=388      len_contig=4640719      sumLogProb=-15.961      meanLogProb=-0.04135     meanLogProb_scaled=-1.919e-05  

All walks len: [388]
All contigs len: [4640719]

No edges left in the subgraph. Stopping...
elapsed time (get_walks): 0h 0m 1s
Loading reads...
Done!
elapsed time (get_contigs): 0h 0m 0s
elapsed time (total): 0h 0m 1s
Found contigs for example!
Model used: weights/weights.pt
Assembly saved in: example/hifiasm
==================================================
Pipeline completed successfully!
==================================================
```

---

## 5. Stored Data Files and Target Locations

All files have been pushed to the remote repository `https://github.com/lavanyamathur/development-team2.git` under branch `abhiraj/baseline-results`.

### E. coli K12 (Paper Reproduction example)
Located under: `results/paper-reproduction/`
- **Resolved GNNome Assembly:** [0_assembly.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/0_assembly.fasta)
- **Native Hifiasm Assembly:** [ecoli_assembly.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/ecoli_assembly.fasta)
- **Reference Genomes:** [reference.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/reference.fasta) and [Ecoli_K12_ref.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/Ecoli_K12_ref.fasta)
- **Raven Assembly:** [raven_assembly.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/raven_assembly.fasta)
- **Assembly Graphs (GFA):**
  - [ecoli_asm.bp.raw.r_utg.gfa](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/ecoli_asm.bp.raw.r_utg.gfa)
  - [ecoli_asm.bp.p_ctg.gfa](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/ecoli_asm.bp.p_ctg.gfa)
  - [ecoli_asm.bp.a_ctg.gfa](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/ecoli_asm.bp.a_ctg.gfa)
- **Scoring Output Folder:** [quast_report/](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/paper-reproduction/quast_report/)

### E. coli DH5α (Experiment baseline)
Located under: `results/ecoli-dh5a/full/`
- **Resolved GNNome Assembly:** [0_assembly.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/ecoli-dh5a/full/0_assembly.fasta)
- **Native Raven Assembly:** [CP017100_assembly.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/ecoli-dh5a/full/CP017100_assembly.fasta)
- **Reference Genome:** [CP017100.fasta](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/ecoli-dh5a/full/CP017100.fasta)
- **Assembly Graph (GFA):** [graph_1.gfa](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/ecoli-dh5a/full/graph_1.gfa)
- **Scoring Outputs:**
  - [quast_report/](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/ecoli-dh5a/full/quast_report/) (GNNome scoring results)
  - [classical_raven_quast_report/](file:///wsl.localhost/Ubuntu/home/abhiraj_arya/research/development-team2/results/ecoli-dh5a/full/classical_raven_quast_report/) (Native Raven scoring results)
