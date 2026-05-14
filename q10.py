from pathlib import Path

from Bio import PDB

# Step 1: Create a PDB parser
parser = PDB.PDBParser(QUIET=True)

# Step 2: Load a protein structure from a local file
pdb_id = "1TUP"
pdb_file = Path(f"pdb{pdb_id.lower()}.ent")

if not pdb_file.exists():
    pdbl = PDB.PDBList()
    pdb_file = Path(pdbl.retrieve_pdb_file(pdb_id, pdir=".", file_format="pdb"))

structure = parser.get_structure("protein", pdb_file)

# Step 3: Access model and chain
model = structure[0]
chain = model["A"]

# Step 4: Print residues in chain
print(f"Chain {chain.id}:")
for residue in chain:
    print(residue)

# Step 5: Save structure for visualization
io = PDB.PDBIO()
io.set_structure(structure)
io.save("output.pdb")
