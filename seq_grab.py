#TAKES SEQUENCES FROM ASSEMBLED GENOME

from Bio import SeqIO
import sys
import re
import numpy as np

genome = sys.argv[1]
scaffold = sys.argv[2]
start = sys.argv[3]
end = sys.argv[4]
output = sys.argv[5]
GEN = SeqIO.parse(genome, format = 'fasta')
outfile = open(output, 'w')

seqs = []

for rec in GEN:
    seqs.append(str(rec.seq))

i = int(scaffold) - 1
a = int(start) - 1
b = int(end)    
sequence = seqs[i][a:b]
        
outfile.write(sequence)
outfile.write('\n')
outfile.close()
