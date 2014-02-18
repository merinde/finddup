# prints files with size in bytes from current directory

import os, sys
from os.path import join, getsize

#glob
#print '''First the file with a specific extentions are 
#printed. In this case .py files.'''
#print glob.glob('*.py')

dirpath = os.getcwd()
listdir = os.listdir( dirpath )

'''from os.path import join, getsize
for root, dirs, files in os.walk(dirpath):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"
    if 'CVS' in dirs:
        dirs.remove('CVS') # don't visit CVS directories'''

for file in listdir:
    print file, sum(getsize(file) for name in file)

