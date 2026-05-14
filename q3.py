# Using a SeqRecord object, write the DNA sequence along with its annotations
# to a GenBank file format.

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dna_sequence = Seq("ATGCGTACGTAGCTAGCTAG")

record = SeqRecord(
    dna_sequence,
    id="seq1",
    name="Example_Gene",
    description="An example DNA sequence for gene annotation.",
    annotations={
        "molecule_type": "DNA",
        "gene": "ExampleGene",
        "function": "Hypothetical protein",
    },
)

output_file_path = r"C:\Users\souri\Downloads\genbank_1.gb"

with open(output_file_path, "w") as output_file:
    SeqIO.write(record, output_file, "genbank")

print("GenBank file was written.")

with open(output_file_path, "r") as input_file:
    record_read = SeqIO.read(input_file, "genbank")

print("\nContents of the GenBank file:")
print(record_read)
