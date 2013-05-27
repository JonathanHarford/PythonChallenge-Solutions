# http://www.pythonchallenge.com/pc/def/integrity.html
# http://www.pythonchallenge.com/pcc/return/good.html:huge:file
# working hard?
# What is the missing link?
# inflate
#
# Answer:

from bz2 import decompress

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print(decompress(un))
print(decompress(pw))

# import code; code.interact(local=locals())
