seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG' 

start_codon = 'AUG'
stop_codon = ['UAA','UAG','UGA']

largest_orf = ''

for i in range(len(seq) - 2):
    if seq[i:i+3] == start_codon:
        for j in range(i + 3,len(seq) - 2,3):
            condon = seq[j:j+3]

            if condon in stop_codon:
                current_orf = seq[i:j+3]

                if len(current_orf) > len(largest_orf):
                    largest_orf = current_orf
                    break
print("Largest ORF:", largest_orf)
print("Length:", len(largest_orf))