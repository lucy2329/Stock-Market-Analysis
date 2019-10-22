fp = open('complete.txt','r')

op = open('nonifty.txt', 'w+')

#s = {'NSEMIDCAP', 'NSEIT'}

line = fp.readline()
#words = line.split(',')
#if('NIFTY' in words[0]):
#		pass
#else:
#	op.write(line)

lst = []

while line:
	line = fp.readline()
	words = line.split(',')	
	#if('NIFTY' in words[0] or words[0] in s or len(words) != 7):
	if(len(words) != 7):
		continue
	else :
		found = 0
		for x in range(len(words)):
			if(words[x] == '-'):
				found = 1
		if(found == 0):
			if(len(lst) == 0):
				lst.append(line)
			else:
				prev = lst[-1]
				words_prev = prev.split(',')
				if(words_prev[0] == words[0] or line == prev):
					if(words_prev[6] < words[6]):
						lst.pop()
						lst.append(line)
				else:
					lst.append(line)

for line in lst:
	op.write(line)
	

op.close()
fp.close()

