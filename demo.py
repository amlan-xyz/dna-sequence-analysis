from Bio.Seq import Seq
from Bio import Entrez, SeqIO
Entrez.email="amlansaikia1918@gmail.com"
handle = Entrez.efetch(db="nucleotide", id="AY851612", rettype="gb", retmode="text")
recs=list(SeqIO.parse(handle,'gb'))
handle.close()
print(recs)
covid_dna=recs[0].seq
# print(covid_dna)
print(f'The genome of Covid -19 consist of {len(covid_dna)} nucleotides')

# from Bio.SeqUtils import gc_fraction
# print(gc_fraction(covid_dna))

# count_nucleotides={
# 	'A': covid_dna.count('A'),
#  	'T': covid_dna.count('T'),
# 	'C': covid_dna.count('C'),
# 	'G': covid_dna.count('G'),
# }
# print(count_nucleotides)

# import matplotlib.pyplot as plt
# width=0.5
# print(plt.bar(count_nucleotides.keys(),count_nucleotides.values(),width,color=['b','r','m','c']))
# print(plt.xlabel('Nucleotide'))
# print(plt.ylabel('Frequency'))
# print(plt.title('Nucleotide Frequency'))

# transcription
covid_mrna=covid_dna.transcribe()
print(covid_mrna)

# translation

covid_aa=covid_mrna.translate()
print(covid_aa)

#most common amino acids
print("##########most common amino acids############")

from collections import Counter
common_amino=Counter(covid_aa)
common_amino.most_common(10)