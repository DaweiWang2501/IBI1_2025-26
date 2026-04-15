# Average residue masses in atomic mass units (amu)
AMINO_ACID_MASSES = {
    'A': 89.09,   # Alanine
    'R': 174.20,  # Arginine
    'N': 132.12,  # Asparagine
    'D': 133.10,  # Aspartic acid
    'C': 121.15,  # Cysteine
    'E': 147.13,  # Glutamic acid
    'Q': 146.15,  # Glutamine
    'G': 75.07,   # Glycine
    'H': 155.16,  # Histidine
    'I': 131.17,  # Isoleucine
    'L': 131.17,  # Leucine
    'K': 146.19,  # Lysine
    'M': 149.21,  # Methionine
    'F': 165.19,  # Phenylalanine
    'P': 115.13,  # Proline
    'S': 105.09,  # Serine
    'T': 119.12,  # Threonine
    'W': 204.23,  # Tryptophan
    'Y': 181.19,  # Tyrosine
    'V': 117.15   # Valine
}


def predict_protein_mass(sequence: str) -> float:

    sequence = sequence.strip().upper()

    total_mass = 0.0
    for amino_acid in sequence:
        if amino_acid not in AMINO_ACID_MASSES:
            raise ValueError(
                f"Error: amino acid '{amino_acid}' has no recorded mass."
            )
        total_mass += AMINO_ACID_MASSES[amino_acid]

    return total_mass


# Example function call
if __name__ == "__main__":
    example_sequence = "MKTFFV"
    try:
        mass = predict_protein_mass(example_sequence)
        print(f"Sequence: {example_sequence}")
        print(f"Predicted protein mass: {mass:.2f} amu")
    except ValueError as error:
        print(error)
