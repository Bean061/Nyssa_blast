#import Bio
#from Bio import SeqIO

#inFile = open('/Users/zhouwenbin/tools/biopython-1.68/change_name_tree/1.fasta','r')
#fw=open("/Users/zhouwenbin/tools/biopython-1.68/change_name_tree/results.txt",'w')

#for record in SeqIO.parse(inFile,'fasta'):
#	fw.write (record.id + '\n')

#fw.close()


import xlrd
wb = xlrd.open_workbook('/Users/zhouwenbin/tools/biopython-1.68/1.xls') # open the excel file
f1=open("/Users/zhouwenbin/tools/biopython-1.68/tree_result.txt",'r') # open the the .tre file.
fw=open("/Users/zhouwenbin/tools/biopython-1.68/change_name_tree/result_for_tree.txt",'w')  #you can change your output file name here.

s = len(f1.readlines())
f1.close()

f1=open("/Users/zhouwenbin/tools/biopython-1.68/tree_result.txt",'r')
sum = ""
for i in range(s):
    text = f1.readline()
    sh = wb.sheet_by_index(0)
    for row in range(sh.nrows):
        text = text.replace(str(sh.cell_value(row,0)),str(sh.cell_value(row,1)))
    sum = text
#dic[str(sh.cell_value(row,0))]=str(sh.cell_value(row,1))
    fw.write (sum)


fw.close()
f1.close()
