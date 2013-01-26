__author__ = 'Admin'

#http://www.voidspace.org.uk/python/modules.shtml#pycrypto

from Crypto.Cipher import AES
from Crypto import Random

def cbc_mode():
    key = b'Sixteen byte key'
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(b'Attack at dawn')
    return 0

print cbc_mode();