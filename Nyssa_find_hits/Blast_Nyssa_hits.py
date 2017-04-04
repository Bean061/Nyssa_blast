from Bio import SeqIO
from Bio.Seq import Seq
import subprocess
import os
from Bio.Blast import NCBIXML


# reading all the sequences.
outfile = 'filtered.fa'   #output file name. Changable
source = 'Nyssa_ursina_SCO.fasta'	# Searching file. Changable
primer = '64 pairs of selected_primers_for_Nyssa_genus.fasta'	# Primer files. Changable
i = 0
for sub in SeqIO.parse(primer, "fasta"):
    sub1 = sub.seq

    # reading the sequences from database based on primer sequence!!!!
    for seq_record in SeqIO.parse(source, "fasta"):
        if sub1 in seq_record.seq:
            sum1 = seq_record
            i = i + 1
            SeqIO.write(sum1, 'filtered' + str(i) + '.fa', 'fasta') #save file as.

#cat_cmd = ['cat', '*.fa', '>', 'all.fa']

subprocess.call(['cd /Users/zhouwenbin/tools/biopython-1.68'], shell = True)
subprocess.call(['cat *.fa > all.fa'], shell = True)



#Blast. Change the directory of blast if necessary.
cmd = "/Users/zhouwenbin/tools/ncbi-blast-2.6.0+/bin/blastn -query /Users/zhouwenbin/tools/biopython-1.68/all.fa -db /Users/zhouwenbin/tools/ncbi-blast-2.6.0+/ctg/ctg -out output3.xml -outfmt 5"
os.system(cmd)



#Parse the result. Get the Query and Hit sequence.
#m = 0
save_file = open("Hit_sequence.fasta", "w")
results = open("output.xml", "r")  # Read your output file.
blast_records = NCBIXML.parse(results)
for blast_record in blast_records:
    blast_record
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 0.01:
                #print(hsp.num_alignments)
                #print(dir(hsp))
                #print('****Alignment****')
                #print('sequence:', alignment.accession)
                #print('length:', alignment.length)
                #print('score:', alignment.score)
                #print('gaps:', alignment.gaps)
                #print('e value:', hsp.expect)
                #print(hsp.query[0:90] + '...')
                #print(hsp.match[0:90] + '...')
                #print(hsp.sbjct)
                #print(hsp.hit)
                #print(dir(alignment))
                sum2 = '>' + alignment.accession + '\n' + hsp.sbjct + '\n'
                #sum2 = hsp.sbjct
                #m = m + 1
                #print(sum2)
                #SeqIO.write(sum2, 'Subject' + str(m) + '.fa', 'fasta')
                save_file.write(sum2)

results.close()
save_file.close()
#blast_qresult = SearchIO.parse('output.xml', 'blast-xml')
