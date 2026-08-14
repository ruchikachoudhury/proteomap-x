from pathlib import Path

import pytest
from proteomapx.variant_parser import parse_mutation_file


def test_parse_mutation_file():
    # take the csv to test the function
    filepath = Path(
        "C:\\Users\\thisi\\Bioinformatics\\Projects\\proteomap-x\\data\\examples\\braf_multivariant.csv"
    )
    # file path is stored in filepath
    mutation_records = parse_mutation_file(filepath)
    # parse the mutation file and store the result in mutation_records

    print(f"Loaded {len(mutation_records)} mutations successfully.\n")

    for mutation in mutation_records:
        print(mutation)


def test_valid_mutation_file():
    csv_file = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "examples"
        / "braf_multivariant.csv"
    )

    records = parse_mutation_file(csv_file)

    assert len(records) == 4
    assert records[0].gene == "BRAF"
    assert records[1].hgvs_p == "p.Leu597Arg"


def test_missing_required_column(tmp_path):
    csv_file = tmp_path / "invalid.csv"

    csv_file.write_text("sample_id,gene,hgvs_p\nPATIENT_001,BRAF,p.Val600Glu\n")

    with pytest.raises(ValueError):
        parse_mutation_file(csv_file)


def test_multiple_mutations_same_gene():
    csv_file = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "examples"
        / "braf_multivariant.csv"
    )

    records = parse_mutation_file(csv_file)

    braf_records = [
        record
        for record in records
        if record.sample_id == "PATIENT_001" and record.gene == "BRAF"
    ]

    assert len(braf_records) == 2
    assert braf_records[0].sample_id == braf_records[1].sample_id
    assert braf_records[0].gene == braf_records[1].gene
