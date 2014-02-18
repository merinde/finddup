# encoding: utf-8
import os, sys, hashlib
from sys import argv
from os.path import join, getsize, isdir

dirpath = os.getcwd() 
listdir = os.listdir( dirpath )

def md5sum(file_name):
    """This returns the hexadecimal md5sum of the input file."""
    f = open(file_name, mode='rb')
    h = hashlib.md5()
    h.update(f.read())
    return h.hexdigest()


## Scan of local directory.
for f in listdir:
   if not isdir(f):
      print "File: ", f,
      print "bytes:", sum(getsize(f) for name in f)
      print "MD5:", md5sum(f)
