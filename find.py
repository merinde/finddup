# copy of finddup-v8.2
# by Michel marcon aka cmic
##############################
#

import getopt, argparse, hashlib, sys, os # os.path, os.walk
from sys import argv

def md5sum(file_name):
    f = open(file_name, mode='r')
    h = hashlib.md5()
    for buf in f.read(128):
        h.update(buf.encode())
    return h.hexdigest()

dir_opt = os.getcwd()

"""if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', 
                        help="long listing without group information")
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help="increase output verbosity")
    parser.add_argument('-a', '--all', action='store_true',
                        help="list normal and hardlinked files")
    args = parser.parse_args()

all_opt=[]
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        (os.path.join(root, name))
    for name in dirs:
        (os.path.join(root, name))
        
print "Files in", dir_opt, ":" 
"""

#print "Enter filename:"
#file_name = raw_input("> ")

for file_name in sys.argv:
    print md5sum(file_name);
