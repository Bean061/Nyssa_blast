from Bio import SeqIO
from Bio.Seq import Seq
import xlrd
import os


path = "/Users/zhouwenbin/tools/biopython-1.68/For_3_test/split_seq"
os.mkdir(path)
for test in SeqIO.parse('PNINRA310AU.fasta','fasta'):
	print test.description
	file = "/Users/zhouwenbin/tools/biopython-1.68/For_3_test/split_seq/" + test.description
	f1 = open(file, 'w')
	SeqIO.write(test, f1, "fasta")
	f1.close()