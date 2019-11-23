import os

allfiles = os.listdir('all/')

op = open("complete.txt",'w+')

for i in allfiles :
	fp = open('all/'+i,"r")

	line = fp.readline()
	op.write(line)

	
	while line:
		line = fp.readline()
		op.write(line)

	fp.close()
	
op.close()