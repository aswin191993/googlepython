dict={}
dict['a'] = 'apple'
dict['b'] = 'baby'
dict['c'] = 'cat'

if 'a' in dict:
	print dict['a']

f=open('foo.txt','rU')
for line in f:
	print line
f.close()
