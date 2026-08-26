import re

from proteomapx.models import ProteinChange

AMINO_ACIDS_1 = set("ARNDCQEGHILKMFPSTWYV")

AMINO_ACIDS_3_TO_1 = {
    "Ala": "A",
    "Arg": "R",
    "Asn": "N",
    "Asp": "D",
    "Cys": "C",
    "Gln": "Q",
    "Glu": "E",
    "Gly": "G",
    "His": "H",
    "Ile": "I",
    "Leu": "L",
    "Lys": "K",
    "Met": "M",
    "Phe": "F",
    "Pro": "P",
    "Ser": "S",
    "Thr": "T",
    "Trp": "W",
    "Tyr": "Y",
    "Val": "V",
}


ONE_LETTER_PATTERN = re.compile(
    r"p\.([ARNDCQEGHILKMFPSTWYV])(\d+)([ARNDCQEGHILKMFPSTWYV])"
)

THREE_LETTER_PATTERN = re.compile(
    r"p\."
    r"(Ala|Arg|Asn|Asp|Cys|Gln|Glu|Gly|His|Ile|Leu|Lys|Met|Phe|Pro|Ser|Thr|Trp|Tyr|Val)"
    r"(\d+)"
    r"(Ala|Arg|Asn|Asp|Cys|Gln|Glu|Gly|His|Ile|Leu|Lys|Met|Phe|Pro|Ser|Thr|Trp|Tyr|Val)"
)


def parse_hgvs_protein(mutation: str) -> ProteinChange:
    mutation = mutation.strip()

    one_letter_match = ONE_LETTER_PATTERN.fullmatch(mutation)

    if one_letter_match:
        original_aa = one_letter_match.group(1)
        position = int(one_letter_match.group(2))
        mutant_aa = one_letter_match.group(3)

        return ProteinChange(
            original_aa=original_aa,
            position=position,
            mutant_aa=mutant_aa,
            hgvs_p=mutation,
        )

    three_letter_match = THREE_LETTER_PATTERN.fullmatch(mutation)

    if three_letter_match:
        original_aa = AMINO_ACIDS_3_TO_1[three_letter_match.group(1)]
        position = int(three_letter_match.group(2))
        mutant_aa = AMINO_ACIDS_3_TO_1[three_letter_match.group(3)]

        return ProteinChange(
            original_aa=original_aa,
            position=position,
            mutant_aa=mutant_aa,
            hgvs_p=mutation,
        )

    raise ValueError(f"Invalid protein HGVS mutation: {mutation}")
