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

for file_name in sys.argv:
    print md5sum(file_name)

