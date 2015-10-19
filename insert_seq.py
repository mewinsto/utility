##INSERTS SEQUENCES FROM .PHY FILE INTO .XML FILE TO RUN BEAST
#SPECIFICALLY, IT MAKES THE TAXA SEQUENCE LINES WHICH CAN BE EASILY MADE INTO AN .XML FILE WITH HEAD AND TAIL COMMANDS (AND XML TEMPLATE)
#FIRST ARGUMENT IS .PHY FILE, SECOND IS XML TEMPLATE, THIRD IS OUTFILE

from Bio import SeqIO
import sys
import re
import numpy as np

phylip = sys.argv[1]
XML = sys.argv[2]
outfile = sys.argv[3]
xml_file = open(XML).readlines()
reader = SeqIO.parse(phylip, format = 'phylip')
INDEX = open(phylip).readlines()
new_xml = open(outfile, 'w')

index = []
seqs = []

for rec in reader:
    seqs.append(str(rec.seq))
    
for line in INDEX[1:]:
    a = line.lstrip().rstrip().split(" ")
    index.append(a[0])

xml_index = ['seq_' + s + '"' for s in index]
    
for line in xml_file:
    for i in range(len(xml_index)):
        if xml_index[i] in line:
            new_seq_string = '                    <sequence id="' + xml_index[i] + '" taxon="' + index[i] + '" totalcount="4" value="' + seqs[i] + '"/>'
            new_xml.write(new_seq_string)
            new_xml.write('\n')
            
new_xml.close()       
