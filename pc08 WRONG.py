# http://www.pythonchallenge.com/pc/def/integrity.html
# working hard?
# What is the missing link?
# inflate
#
# Answer:

def decode(str,f):
    return f(str)

from base64 import b64decode
from binascii import b2a_uu, b2a_base64, b2a_qp, b2a_hqx

keyring = [b2a_uu, b2a_base64, b2a_qp, b2a_hqx, b64decode]
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

un = b64decode(un)

for key in keyring:
    unlocked = decode(un,key)
    print(key.__name__)
    print(unlocked)
    print(repr(unlocked))

# print(b32decode(un)) # Incorrect Padding
# print(b16decode(un)) # Non-base16 digit found
# print(quopri.decodestring(un)) # Appears to return source.
# rledecode_hqx returns source


# import code; code.interact(local=locals())
