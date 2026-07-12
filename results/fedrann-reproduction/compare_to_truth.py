import pysam
import re
from collections import defaultdict

# --- Configuration ---
SAM_PATH = "/home/akshat/reads/subset_50k_aligned.sam"
OVERLAPS_TSV = "/home/akshat/reads/subset_output_50k/overlaps.tsv"
MIN_READ_LENGTH = 5000
MIN_ALIGNED_FRACTION = 0.5
MIN_MAPQ = 30

# --- Step 1: Parse SAM file, apply filters, extract read intervals ---
print("Parsing SAM file...")
read_intervals = {}  # read_name -> (chrom, start, end, strand)
samfile = pysam.AlignmentFile(SAM_PATH, "r")

total = 0
passed = 0
for read in samfile.fetch(until_eof=True):
    total += 1
    if read.is_unmapped:
        continue
    if read.mapping_quality < MIN_MAPQ:
        continue

    read_length = read.query_length if read.query_length else read.infer_read_length()
    if read_length is None or read_length < MIN_READ_LENGTH:
        continue

    aligned_length = read.query_alignment_length
    if aligned_length is None or (aligned_length / read_length) < MIN_ALIGNED_FRACTION:
        continue

    chrom = read.reference_name
    start = read.reference_start
    end = read.reference_end
    strand = "-" if read.is_reverse else "+"

    read_intervals[read.query_name] = (chrom, start, end, strand)
    passed += 1

samfile.close()
print(f"Total alignment records: {total}")
print(f"Reads passing filters: {passed}")

# --- Step 2: Build truth overlap graph ---
# Two reads truly overlap if their genomic intervals overlap on the same chromosome
print("Building truth overlap graph...")
by_chrom = defaultdict(list)
for name, (chrom, start, end, strand) in read_intervals.items():
    by_chrom[chrom].append((start, end, name))

truth_edges = set()
for chrom, intervals in by_chrom.items():
    intervals.sort()
    for i in range(len(intervals)):
        start_i, end_i, name_i = intervals[i]
        for j in range(i + 1, len(intervals)):
            start_j, end_j, name_j = intervals[j]
            if start_j >= end_i:
                break  # sorted by start, no further overlaps possible
            # overlap exists
            edge = tuple(sorted([name_i, name_j]))
            truth_edges.add(edge)

print(f"Truth graph edges: {len(truth_edges)}")

# --- Step 3: Parse Fedrann's predicted overlaps ---
print("Parsing Fedrann overlaps.tsv...")
predicted_edges = set()
read_name_pattern = re.compile(r'^(.*?)(?:\.\d+)?$')  # in case of suffix mismatches

with open(OVERLAPS_TSV) as f:
    header = f.readline()
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) < 4:
            continue
        query_name, query_orient, target_name, target_orient = parts[0], parts[1], parts[2], parts[3]
        edge = tuple(sorted([query_name, target_name]))
        predicted_edges.add(edge)

print(f"Predicted edges (Fedrann): {len(predicted_edges)}")

# --- Step 4: Compute metrics ---
print("\n--- Computing metrics ---")

correct_edges = predicted_edges & truth_edges
incorrect_edges = predicted_edges - truth_edges

error_rate = len(incorrect_edges) / len(predicted_edges) if predicted_edges else float('nan')

print(f"Correct edges: {len(correct_edges)}")
print(f"Incorrect edges: {len(incorrect_edges)}")
print(f"Error rate: {error_rate:.4f}")

# Recall: how many truth edges did we recover?
recovered = truth_edges & predicted_edges
recall = len(recovered) / len(truth_edges) if truth_edges else float('nan')
print(f"Recall (truth edges recovered): {recall:.4f}")

print("\nDone.")
