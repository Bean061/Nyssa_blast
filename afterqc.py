import os, subprocess

read1 = "/Users/xianglab/tools/NGSdatatools/Single4848Chip_R1.fastq"
read2 = "/Users/xianglab/tools/NGSdatatools/Single4848Chip_R2.fastq"

path_after = "/Users/xianglab/Tools/NGSdatatools/AfterQC-master/after.py"
for i in range(0,200,20):     
	process_folder ="/Users/xianglab/Tools/NGSdatatools/AfterQC-master/afterqc_result_" + str(i)     
	os.mkdir(process_folder)
	result_good = process_folder + "/good"
	result_bad = process_folder + "/bad"
	result_report = process_folder + "/report"
	os.mkdir(result_good)
	os.mkdir(result_bad)
	os.mkdir(result_report)
	cmd1 = ['python', path_after, '-1', read1, '-2', read2, '-f', '0', '-t', str(i), '-q', '20', '-u', '3', '-g', result_good, '-b', result_bad, '-r', result_report]
	subprocess.check_output(cmd1)