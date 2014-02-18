# encoding: utf-8
import os, sys, hashlib 
from sys import argv
from os.path import join, getsize, isdir
from collections import Counter, OrderedDict

dirpath = os.getcwd() 
listdir = os.listdir( dirpath )

def md5sum(file_name):
    """This returns the hexadecimal md5sum of the input file."""
    f = open(file_name, mode='rb')
    h = hashlib.md5()
    h.update(f.read())
    return h.hexdigest()

#Create an empty list.
hashlist=[]
hashmap={}

## Scan of local directory.
for f in listdir:
   if not isdir(f):
      "File: ", f,
      "bytes:", sum(getsize(f) for name in f)
      "MD5:", md5sum(f) 
      hash = md5sum(f)
      #print "md5(%16s) is %s" % (f,hash)  #Uncomment for debugging.
      
      #Append to that empty list.
      hashlist=hashlist+[hash]
      
      #Does it exist in the hashmap already?
      try:
          old=hashmap[hash];
          print "%s and %s have the same md5, %s" % (f,old,hash);
      except:
          #Record doesn't exist, so we add it to the hashmap.
          hashmap[hash]=f;


#None of this is needed anymore because we use a hashmap.
# Sort the list, so that equal records are next to eachother.
# hashlist.sort();

# #Scan the list for duplicates.
# for i in range(0, len(hashlist)-1):
#    if hashlist[i]==hashlist[i+1]:
#       print "Multiple files hash to %s." % hashlist[i]
