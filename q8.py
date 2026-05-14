from Bio import AlignIO
import subprocess

# Define sequences
seq1 = """>seq1
ATGCGTACGTA
"""
seq2 = """>seq2
ATGCGTACGTC
"""
seq3 = """>seq3
ATGCGTACGAG
"""

# Write sequences to file
with open("fasta8.fasta", "w") as f:
    f.write(seq1)
    f.write(seq2)
    f.write(seq3)

# MUSCLE executable path
muscle_exe = r"C:\Users\souri\Downloads\muscle-win64.v5.3 (1).exe"

# Run MUSCLE
subprocess.run(
    [muscle_exe, "-align", "fasta8.fasta", "-output", "aligned_sequences.fasta"],
    check=True
)

# Read alignment
alignment = AlignIO.read("aligned_sequences.fasta", "fasta")

# Print result
print(alignment)
