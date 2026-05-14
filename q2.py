from Bio import SeqIO


def read_fasta(file_path):
    for record in SeqIO.parse(file_path, "fasta"):
        print(f"Description: {record.description}")
        print(f"Sequence: {record.seq}")
        print()


fasta_file = r"C:\Users\souri\Downloads\fasta_1 (1).fasta"
read_fasta(fasta_file)
