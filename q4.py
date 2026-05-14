# Given a FASTA file, write a Python script that reads the file and converts it into GenBank format,
# while preserving the sequence and annotations.

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

def convert_fasta_file(fasta_file,genbank_file):
    records=[]
    for record in SeqIO.parse(fasta_file,"fasta"):
        seq=record.seq
        desc=record.description
        
        genbank_record=SeqRecord(
            seq,
            id=record.id,
            name="ExampleGene",
            description=desc,    
            annotations={
                'molecule_type':"DNA",
                'gene':"Example_Gene",
                'function':"Hypothetical Protien"
            }
        )

        records.append(genbank_record)

    with open(genbank_file,'w'):
        SeqIO.write(records,genbank_file,"genbank")
    print(f"All FASTA sequences converted to GenBank format and saved as {genbank_file}")

    with open(genbank_file, 'r') as f:
        print(f.read())

fasta_file= r"C:\Users\souri\Downloads\fasta_1 (1).fasta"
genbank_file= r"C:\Users\souri\Downloads\genbank_1.gb"

convert_fasta_file(fasta_file, genbank_file)