import os

op = open("splits.txt",'w+')

for year in range (1995 ,2020):
	y = str(year)
	
	fp = open(y+'splits.txt',"r")

	line = fp.readline()
	op.write(line)

	
	while line:
		line = fp.readline()
		op.write(line)

	fp.close()
		
op.close()