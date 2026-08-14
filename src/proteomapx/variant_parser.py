import csv
from dataclasses import dataclass
from pathlib import (
    Path,  #ruff check "ruff check --select I --fix proteomap-x/src/proteomapx/variant_parser.py" to fix import order
)


@dataclass
class Mutationrecord:
    sample_id: str
    gene: str
    hgvs_p: str
    protein_accession: str #initializing the Mutationrecord dataclass with the required fields to store mutation information.

required_columns = {
    "sample-id",
    "gene",
    "hgvs_p",
    "protein_accession"
} #defining the set of required columns in the CSV file to ensure that the input data is valid and contains all necessary information for further processing.

def parse_mutation_file(filepath: Path):

    with filepath.open("r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
            raise ValueError(f"Missing required columns in {filepath}. Required columns: {required_columns}")#reading through the document


        parsed_records = [] #list to store the parsed mutation records
        for row_number, row in enumerate(reader, start=2):  # Start at 2 to account for header row
            mutation_record = Mutationrecord(
                sample_id=row["sample-id"].strip(),
                gene=row["gene"].strip(),
                hgvs_p=row["hgvs_p"].strip(),
                protein_accession=row["protein_accession"].strip()
            )
            if not mutation_record.sample_id or not mutation_record.gene or not mutation_record.hgvs_p or not mutation_record.protein_accession:
                raise ValueError(f"Missing required data in row {row_number} of {filepath}. All fields must be non-empty.")
            parsed_records.append(mutation_record) #converted csv file into a list of Mutationrecord objects, which can be used for further analysis or processing.

    return parsed_records
