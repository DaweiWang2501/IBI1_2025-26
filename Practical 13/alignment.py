#!/usr/bin/env python3
"""
Practical 13: simple non-gapped global protein alignment.

The script reads FASTA protein sequences and a BLOSUM62 matrix, then reports
raw BLOSUM score, score per residue, and percentage identity. It is intentionally
simple: sequences must be the same length and no gaps are introduced.
"""

from __future__ import annotations

import itertools
import random
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

AMINO_ACIDS = "ARNDCQEGHILKMFPSTWYV"


def read_fasta(path: str | Path) -> Tuple[str, str]:
    """Return (header, sequence) from a one-record FASTA file."""
    path = Path(path)
    header = ""
    parts: List[str] = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                header = line[1:]
            else:
                parts.append(line.replace(" ", "").upper())
    if not header or not parts:
        raise ValueError(f"{path} is not a valid one-record FASTA file")
    return header, "".join(parts)


def write_fasta(path: str | Path, header: str, sequence: str, width: int = 60) -> None:
    """Write a sequence to FASTA format."""
    with Path(path).open("w") as handle:
        handle.write(f">{header}\n")
        for i in range(0, len(sequence), width):
            handle.write(sequence[i : i + width] + "\n")


def read_blosum(path: str | Path) -> Dict[Tuple[str, str], int]:
    """Read a whitespace-separated BLOSUM-style substitution matrix."""
    rows = []
    with Path(path).open() as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            rows.append(line.split())

    headers = rows[0]
    matrix: Dict[Tuple[str, str], int] = {}
    for row in rows[1:]:
        aa = row[0]
        scores = list(map(int, row[1:]))
        if len(scores) != len(headers):
            raise ValueError("BLOSUM matrix has an inconsistent number of columns")
        for bb, value in zip(headers, scores):
            matrix[(aa, bb)] = value
    return matrix


def compare(seq1: str, seq2: str, matrix: Dict[Tuple[str, str], int]) -> Dict[str, float | int]:
    """Compare two equal-length protein sequences with no gaps."""
    if len(seq1) != len(seq2):
        raise ValueError("This non-gapped global alignment requires equal-length sequences")

    score = 0
    identical = 0
    for aa, bb in zip(seq1, seq2):
        try:
            score += matrix[(aa, bb)]
        except KeyError as exc:
            raise ValueError(f"Unsupported amino acid pair: {aa!r}, {bb!r}") from exc
        if aa == bb:
            identical += 1

    length = len(seq1)
    return {
        "length": length,
        "score": score,
        "score_per_residue": score / length,
        "identical": identical,
        "percent_identity": 100 * identical / length,
    }


def make_random_protein(length: int, seed: int = 13) -> str:
    """Generate a reproducible random protein sequence."""
    rng = random.Random(seed)
    return "".join(rng.choice(AMINO_ACIDS) for _ in range(length))


def alignment_midline(seq1: str, seq2: str) -> str:
    """Return a simple visual identity line: | for identical, space otherwise."""
    return "".join("|" if a == b else " " for a, b in zip(seq1, seq2))


def print_pairwise_result(name1: str, seq1: str, name2: str, seq2: str, matrix) -> None:
    result = compare(seq1, seq2, matrix)
    print(f"\n{name1} vs {name2}")
    print("-" * (len(name1) + len(name2) + 4))
    print(f"Length:              {result['length']}")
    print(f"BLOSUM62 score:      {result['score']}")
    print(f"Score per residue:   {result['score_per_residue']:.3f}")
    print(f"Identical residues:  {result['identical']}/{result['length']}")
    print(f"Percent identity:    {result['percent_identity']:.2f}%")


def main() -> None:
    base = Path(__file__).resolve().parent
    matrix = read_blosum(base / "BLOSUM62.txt")

    human_name, human_seq = read_fasta(base / "human_DLX5.fasta")
    mouse_name, mouse_seq = read_fasta(base / "mouse_DLX5.fasta")

    random_seq = make_random_protein(len(human_seq), seed=13)
    random_path = base / "random_protein_seed13.fasta"
    write_fasta(random_path, "random_protein_seed13 length=289", random_seq)
    random_name, random_seq = read_fasta(random_path)

    sequences = [
        ("human_DLX5", human_seq),
        ("mouse_DLX5", mouse_seq),
        ("random_seed13", random_seq),
    ]

    print("Practical 13: non-gapped global alignment with BLOSUM62")
    print("Random sequence seed: 13")
    for (name1, seq1), (name2, seq2) in itertools.combinations(sequences, 2):
        print_pairwise_result(name1, seq1, name2, seq2, matrix)


if __name__ == "__main__":
    main()
