# stop_codons.py

INPUT_FILE = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
OUTPUT_FILE = "stop_genes.fa"

START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]


def extract_gene_name(header):
    """
    Try to extract the gene name from a FASTA header.
    Example Ensembl-style headers often contain a field like gene:YBR024W.
    If not found, fall back to the first token after '>'.
    """
    header = header[1:].strip()  # remove '>'
    fields = header.split()

    for field in fields:
        if field.startswith("gene:"):
            return field.split(":", 1)[1]

    return fields[0]


def find_in_frame_stop_codons(sequence):
    """
    Find which stop codons are used by ORFs that start with ATG.
    For each ATG start, only the first in-frame stop codon is counted.
    Returns a list such as ['TAA', 'TGA'].
    """
    found = set()

    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == START_CODON:
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]

                if codon in STOP_CODONS:
                    found.add(codon)
                    break

    # keep output order consistent
    return [codon for codon in STOP_CODONS if codon in found]


def write_fasta_sequence(outfile, sequence, width=60):
    """
    Write sequence in FASTA format with fixed line width.
    """
    for i in range(0, len(sequence), width):
        outfile.write(sequence[i:i+width] + "\n")


def main():
    with open(INPUT_FILE, "r") as infile, open(OUTPUT_FILE, "w") as outfile:
        current_header = None
        sequence_parts = []

        for line in infile:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                # process previous record
                if current_header is not None:
                    sequence = "".join(sequence_parts).upper()
                    stop_list = find_in_frame_stop_codons(sequence)

                    if stop_list:
                        gene_name = extract_gene_name(current_header)
                        outfile.write(f">{gene_name} {','.join(stop_list)}\n")
                        write_fasta_sequence(outfile, sequence)

                # start new record
                current_header = line
                sequence_parts = []
            else:
                sequence_parts.append(line)

        # process final record
        if current_header is not None:
            sequence = "".join(sequence_parts).upper()
            stop_list = find_in_frame_stop_codons(sequence)

            if stop_list:
                gene_name = extract_gene_name(current_header)
                outfile.write(f">{gene_name} {','.join(stop_list)}\n")
                write_fasta_sequence(outfile, sequence)

    print(f"Finished. Results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()