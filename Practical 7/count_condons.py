import matplotlib.pyplot as plt

INPUT_FILE = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]


def extract_gene_name(header):
    header = header[1:].strip()
    fields = header.split()

    for field in fields:
        if field.startswith("gene:"):
            return field.split(":", 1)[1]

    return fields[0]


def parse_fasta(filename):
    current_header = None
    sequence_parts = []

    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_header is not None:
                    yield current_header, "".join(sequence_parts).upper()

                current_header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)

        if current_header is not None:
            yield current_header, "".join(sequence_parts).upper()


def find_longest_orf_with_target_stop(sequence, target_stop):
    best_orf = None

    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == START_CODON:
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]

                if codon in STOP_CODONS:
                    if codon == target_stop:
                        current_orf = sequence[i:j+3]
                        if best_orf is None or len(current_orf) > len(best_orf):
                            best_orf = current_orf
                    break

    return best_orf


def count_codons_upstream_of_stop(orf):
    counts = {}
    coding_region = orf[:-3]  # 去掉最后的stop codon

    for i in range(0, len(coding_region), 3):
        codon = coding_region[i:i+3]
        if len(codon) == 3:
            counts[codon] = counts.get(codon, 0) + 1

    return counts


def make_pie_chart(total_counts, target_stop, genes_used):
    labels = list(total_counts.keys())
    sizes = list(total_counts.values())

    fig, ax = plt.subplots(figsize=(12, 12))

    wedges, texts, autotexts = ax.pie(
        sizes,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title(
        f"In-frame codon distribution upstream of {target_stop}\n"
        f"Genes included: {genes_used}"
    )
    ax.axis("equal")

    ax.legend(
        wedges,
        labels,
        title="Codons",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    output_image = f"codon_frequency_{target_stop}.png"
    plt.tight_layout()
    plt.savefig(output_image, dpi=300, bbox_inches="tight")
    plt.close()

    return output_image


def main():
    target_stop = input("Enter one stop codon (TAA, TAG, TGA): ").strip().upper()

    while target_stop not in STOP_CODONS:
        target_stop = input("Invalid input. Please enter TAA, TAG, or TGA: ").strip().upper()

    total_counts = {}
    genes_used = 0

    for header, sequence in parse_fasta(INPUT_FILE):
        best_orf = find_longest_orf_with_target_stop(sequence, target_stop)

        if best_orf is not None:
            genes_used += 1
            codon_counts = count_codons_upstream_of_stop(best_orf)

            for codon, count in codon_counts.items():
                total_counts[codon] = total_counts.get(codon, 0) + count

    if genes_used == 0:
        print(f"No genes found with an ORF ending in {target_stop}.")
        return

    print(f"\nStop codon selected: {target_stop}")
    print(f"Number of genes included: {genes_used}")
    print("\nCodon counts upstream of the selected stop codon:")

    for codon in sorted(total_counts):
        print(f"{codon}: {total_counts[codon]}")

    output_image = make_pie_chart(total_counts, target_stop, genes_used)
    print(f"\nPie chart saved to: {output_image}")


if __name__ == "__main__":
    main()