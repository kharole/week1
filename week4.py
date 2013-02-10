import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q.encode("hex"))    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


c = [
"f20bdba6ff29eed7b046d1df9fb70000".decode("hex"),
"58b1ffb4210a580f748b4ac714c001bd".decode("hex"),
"4a61044426fb515dad3f21f18aa577c0".decode("hex"),
"bdf302936266926ff37dbf7035d5eeb4".decode("hex")
]

po = PaddingOracle()

def padding(n):
    result = "";
    for i in range(n):
        result += chr(n)
    for i in range(16-n):
        result = chr(0) + result
    return result

def guess(m, g):
    result = "";
    for i in range(16-len(m)-1):
        result += chr(0)
    result += chr(g)
    result += m
    return result

def decrypt_block(b):
    m = ""
    for i in range(16):
        m = decrypt_char(m, i+1, b) + m
        #print m.encode("hex")
    return m

def decrypt_char(m, n, b):
    none_g = ""
    for g in range(255):
        g_block = guess(m, g)
        test_c = list(c)
        #print g_block.encode("hex")
        test_c[b-1] = strxor(test_c[b-1], g_block)
        padding_block = padding(n)
        #print padding_block.encode("hex")
        test_c[b-1] = strxor(test_c[b-1], padding_block)
        test = po.query("".join(test_c[0:b+1]))
        if test is None:
            none_g = chr(g)
        if test:
            return chr(g)
    return none_g

def unpad(s):
    n = ord(s[len(s)-1]);
    return s[0:len(s)-n]

#print one_byte_block(1).encode("hex")
#print po.query(iv + c0 + c1 + c2)

#print padding(3).encode("hex")

#print po.query(iv + c0 + c1 + c2)

m = decrypt_block(1) + decrypt_block(2) + decrypt_block(3)

print m
print m.encode('hex')
print unpad(m)

#print "73696672616765".decode("hex")


#print "".join(c[0:1]).encode("hex")
#print "".join(c[0:2]).encode("hex")
#print "".join(c[0:3]).encode("hex")
#print "".join(c[0:4]).encode("hex")