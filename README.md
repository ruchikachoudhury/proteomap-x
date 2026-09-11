ProteoMap-X is a Python-based structural bioinformatics pipeline for processing protein-level disease-associated mutations. The project currently focuses on validating and normalizing protein HGVS variants and preparing structured mutation data for downstream structural analysis.
 
 Rather than only asking, "What disease is associated with this mutation?", we instead ask "How might one or more of these disease-associated muattions alter the physical structure and subsequently the protein dynamics and also could these changes have any implications for known therapeutic interactions?"
The project takes protein-level variants from a patient or sample and progressively maps them from mutation notation -> protein residue -> 3D structure -> structural relationships -> protein dynamics -> disease/clinical information. 
_Drug-discovery extension_
ProteoMap-X can also provide a foundation for in-silico drug studies. For proteins with known therapeutic targets and associated drugs, the pipeline can be extended to compare wild-type and mutant protein–drug interactions through molecular docking and structural analysis.
This could help generate hypotheses about whether disease-associated mutations may alter a drug-binding environment or potentially influence predicted drug–protein interactions.
These computational results would be treated as hypothesis-generating rather than clinical predictions, and could be used to prioritize candidates for subsequent experimental validation.

# Project Status

ProteoMap-X is currently under active development.

# Completed
- Protein-level mutation input and validation
- Modular Python package architecture
- Automated testing

# In Progress
- HGVS protein mutation parsing and normalization

# Planned
- UniProt protein mapping
- PDB/AlphaFold structure retrieval
- Mutation-to-residue 3D mapping
- Multi-mutation spatial analysis
- Protein dynamics analysis using ProDy
- Clinical annotation integration
- Interactive structural visualization
