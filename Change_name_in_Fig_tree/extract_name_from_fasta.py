import numpy
import scipy
import Bio
from Bio import SeqIO

inFile = open('/Users/zhouwenbin/tools/biopython-1.68/change_name_tree/treeseq.fasta','r') #input fasta file.
fw=open("/Users/zhouwenbin/tools/biopython-1.68/change_name_tree/results1.txt",'w') #you can change your output file name here.

for record in SeqIO.parse(inFile,'fasta'):
	fw.write (record.id + '\n')

fw.close()
