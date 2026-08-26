import pytest
from proteomapx.hgvs import parse_hgvs_protein


def test_parse_three_letter_mutation():
    result = parse_hgvs_protein("p.Val600Glu")

    assert result.original_aa == "V"
    assert result.position == 600
    assert result.mutant_aa == "E"
    assert result.hgvs_p == "p.Val600Glu"


def test_parse_one_letter_mutation():
    result = parse_hgvs_protein("p.V600E")

    assert result.original_aa == "V"
    assert result.position == 600
    assert result.mutant_aa == "E"
    assert result.hgvs_p == "p.V600E"


@pytest.mark.parametrize(
    "mutation",
    [
        "p.B600E",
        "p.X600E",
        "p.ValGlu",
        "p.600E",
        "Val600Glu",
        "hello",
        "p.Val600",
    ],
)
def test_invalid_mutations_are_rejected(mutation):
    with pytest.raises(ValueError):
        parse_hgvs_protein(mutation)
