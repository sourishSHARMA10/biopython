# 1 b. Using the Seq class from Biopython, create a DNA sequence object and: i. Slice the sequence to
# extract a specific region (e.g., from index 3 to 10). ii. Concatenate this sequence with another
# sequence. iii. Transcribe and translate the concatenated sequence into RNA and protein sequences.

from Bio.Seq import Seq

dna_sequence=Seq("ATGCTAGCTAGCTAGCTG")

sliced_sequence=dna_sequence[3:10]
print("Sliced Sequence:", sliced_sequence)

another_seq=Seq("GGCTAG")
concatenated_seq=sliced_sequence+another_seq
print("Concatenated Sequence:", concatenated_seq)

rna_seq=concatenated_seq.transcribe()
print("RNA Sequence:", rna_seq)

protein_seq=rna_seq.translate()
print("Protein Sequence:", protein_seq)