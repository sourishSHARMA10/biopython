from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from pathlib import Path

alignment_file = "aligned_sequences.aln"
alignment_path = Path(alignment_file)

if not alignment_path.exists() or alignment_path.stat().st_size == 0:
    raise FileNotFoundError(
        f"{alignment_file} is missing or empty. Add a valid CLUSTAL alignment before running this script."
    )

# Step 1: Load the sequence alignment.
alignment = AlignIO.read(alignment_file, "clustal")

# Step 2: Calculate sequence distances from the alignment.
calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

# Step 3: Build the phylogenetic tree.
constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)

# Step 4: Display the tree in the terminal.
Phylo.draw_ascii(tree)
