#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dict):
	name_stng = '\n'.join(os.listdir(dict))
	spec_lst = re.findall(r'.*__\w+__.*',name_stng)
	spec_file = []
	for name in spec_lst:
		if os.path.isfile(name):
			spec_file.append(os.path.abspath(name))
	return spec_file

def copy_to(paths,dict):
	if not os.path.exists(dict):
		os.makedirs(dict)
	for path in paths:
		shutil.copy(path,dict)

def zip_to(paths,zippath):
	cmd = "zip -j " + zippath
	for path in paths:
		cmd += ' ' + path
	print "Command to run:", cmd
	(status, output) = commands.getstatusoutput(cmd)
	if status:
		sys.stderr.write(output)
		sys.exit(1)
	print output


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  paths = []
  for arg in args:
    paths.extend(get_special_paths(arg))

  if todir == '' and tozip == '':
    print '\n'.join(paths) + '\n'

  if todir:
    copy_to(paths,todir)

  if tozip:
    zip_to(paths,tozip)
  

if __name__ == "__main__":
  main()
