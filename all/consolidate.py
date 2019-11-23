import sys
import glob
import os.path

list_of_files = glob.glob('2019-*.txt')

#print(list_of_files)

for file_name in list_of_files:
	lst=[]
	f = open(file_name, "r")

	print(file_name)

    
    
	
	
	for line in f:
		line.strip()
		#line = line.replace('\n','')
		line = line.replace('//', '')
		lst.append(line)

	f.close()

	f = open("output.txt", "a")

	for line in lst:
		f.write(line)

	f.close()