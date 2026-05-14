# Create a SeqRecord object for a DNA sequence and add annotations for a gene (start, end position,
# description). Modify the annotations and print the updated SeqRecord.

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation

# Create sequence + record
record = SeqRecord(
    Seq("ATGCGTACGTAGCTAGCTAG"),
    id="seq1",
    description="Example DNA"
)
# Add annotations (all in one go)
record.annotations = {
    "gene": "ExampleGene",
    "function": "hypothetical protein",
    "organism": "synthetic organism"
}
# Add feature (gene position)
record.features.append(
    SeqFeature(FeatureLocation(0, 21), type="gene")
) 
# Modify annotation
record.annotations["function"] = "Modified protein"

print(f"ID: {record.id}")
print(f"Name: {record.name}")
print(f"Description: {record.description}")
print(f"Annotations: {record.annotations}")
print(f"Features: {record.features}")