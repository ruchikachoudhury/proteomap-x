from dataclasses import dataclass


@dataclass(frozen=True)
class ProteinChange:
    original_aa: str
    position: int
    mutant_aa: str
    hgvs_p: str
