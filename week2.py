__author__ = 'Admin'

#http://www.voidspace.org.uk/python/modules.shtml#pycrypto

from Crypto.Cipher import AES
from Crypto import Random

import struct

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def pad(s):
    return s

def unpad(s):
    n = ord(s[len(s)-1]);
    return s[0:len(s)-n]

def cbc_mode_dec(key, iv_ct):
    iv = iv_ct[0:16]
    cipher = AES.new(key)
    msg = ''
    for i in range(len(iv_ct)/16-1):
        ct = iv_ct[16*(i+1):16*(i+2)]
        d = cipher.decrypt(ct);
        msg = msg + strxor(d, iv)
        iv = ct
        print msg

    return unpad(msg)

def cbc_mode_enc():
    key = '140b41b22a29beb4061bda66b6747e14'.decode("hex")
    iv = Random.new().read(AES.block_size)
    #cipher = AES.new(key, AES., iv)
    #msg = iv + cipher.encrypt(b'Attack at dawn')
    return 0


def inc_iv(iv):
    a = map(ord,iv)
    iv_int = reduce(lambda x, y: (x<<8) + y, a)
    iv_int = iv_int + 1
    return tost(iv_int)

def tost(i):
    result = []
    while i:
        result.append(chr(i&0xFF))
        i >>= 8
    result.reverse()
    return ''.join(result)

def ctr_mode_dec(key, iv_ct):
    iv = iv_ct[0:16]
    cipher = AES.new(key)
    otp = ''
    for i in range(len(iv_ct)/16):
        otp = otp + cipher.encrypt(iv)
        iv = inc_iv(iv)

    return strxor(otp, iv_ct[16:])


key = '140b41b22a29beb4061bda66b6747e14'.decode("hex")
iv_ct = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode("hex")

print cbc_mode_dec(key, iv_ct)

key = '140b41b22a29beb4061bda66b6747e14'.decode("hex")
iv_ct = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode("hex")

print cbc_mode_dec(key, iv_ct)

key = '36f18357be4dbd77f050515c73fcf9f2'.decode("hex")
iv_ct = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode("hex")

print ctr_mode_dec(key, iv_ct)

key = '36f18357be4dbd77f050515c73fcf9f2'.decode("hex")
iv_ct = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode("hex")

print ctr_mode_dec(key, iv_ct)

