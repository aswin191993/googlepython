import re

str='asswin1999@gmmk.fof'

f = open('foo1.txt' , 'rU')
fname = f.read()
f.close()

match = re.findall(r'as\S+', fname)
#if match:
#	print match.group()
for line in match:
	print line
