# md5 of file specified

import os, sys, hashlib
from sys import argv

dir_opt = os.getcwd()

#print "Enter filename:"
#file_name = raw_input("> ")

def md5sum(file_name):
    f = open(file_name, mode='r')
    h = hashlib.md5()
    for buf in f.read(128):
        h.update(buf.encode())
    return h.hexdigest()

#for file_name in sys.argv:
#    print md5sum(file_name)

## Main ##
if len(sys.argv) < 2:
   print 'No action specified.'
   sys.exit()
if sys.argv[1].startswith('--'):
   option = sys.argv[1][2:]
   # Fetch sys.argv[1] and copy the string except for 1st 2 characters
   if option == 'version':
      print 'Version 1.00'
   elif option == 'v':
      print 'Version 1.00'
   elif option == 'help':
      print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
    --version, --v : Prints the version number and exits
    --help, --h    : Prints this help and exists'''
   else:
      print 'Unknown option.'
   sys.exit()
else:
   for file_name in sys.argv[1:]:
       print md5sum(file_name)

