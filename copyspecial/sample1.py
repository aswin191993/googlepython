import os
import sys

dir = "/home/aswin/googlepython/copyspecial"

filenames = os.listdir(dir)
for file in filenames:
# print text in file 'foo.txt'
	if file == 'foo.txt':
		f=open('foo.txt', 'r')
		temp=f.read()
		print temp
	else:
		print file





