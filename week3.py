import Crypto.Hash.SHA256

__author__ = 'Admin'

import os
from Crypto.Hash import SHA256

filename = "E:/playground/test1.mp4"

def blocks_from_file(filename, blocksize=1024):
    f = open(filename, "rb")
    len = os.path.getsize(filename)
    num_of_blocks = len/blocksize
    if len%blocksize:
        num_of_blocks += 1

    for i in range(num_of_blocks):
        p = (num_of_blocks - i - 1)*blocksize
        size_to_read = blocksize
        if len-p < blocksize:
            size_to_read = len-p
        f.seek(p)
        block = f.read(size_to_read)
        yield block


#t = ''
#for block in blocks_from_file(filename):
#    t = block + t
#    print  len(block)
#
#print t
#
#fout = open("E:/playground/out", "wb")
#fout.write(t)

h = ''
for block in blocks_from_file(filename):
    #print block + h
    #print  len(block + h)
    #print  (block + h).encode('hex')

    #print '++++++++++++++++++++++++++++++++++++++++++++='
    sha256 = SHA256.new(block + h)
    h = sha256.digest()
    #print h.encode('hex')

#print sha256.hexdigest()
#print len()
print h.encode('hex')
