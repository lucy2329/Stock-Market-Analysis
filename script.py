import os

for year in range (1995 ,2020):
	y = str(year)
	allfiles = os.listdir(y+'/')
	#allfiles.remove("all2018.txt")
	op = open(y+"/all"+y+".txt",'w+')

	for i in allfiles :
		fp = open(y+'/'+i,"r")

		line = fp.readline()
		op.write(line)

		
		while line:
			line = fp.readline()
			op.write(line)

		fp.close()
		
	op.close()