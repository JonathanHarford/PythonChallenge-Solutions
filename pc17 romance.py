# http://huge:file@www.pythonchallenge.com/pc/return/romance.html
# ANSWER: http://www.pythonchallenge.com/pcc/return/balloons.html
# TITLE: eat?

# http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345

import urllib2
import urllib
from bz2 import decompress
from re import findall

nuffink = "12345"
infos = []
for i in range(1,200):
    f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + nuffink)
    html = f.read()
    f.close()
    print(html)
    infos.append(findall("info=([^;]+);", f.headers.dict['set-cookie'])[0])
    try:
        nuffink = findall("next busynothing is (\d+)",html)[0]
    except IndexError:
        break
infos = "".join(infos)
# Ah, a bz2 stream.

bz = urllib.unquote_plus(infos)
print(decompress(bz))
# "is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand."

inform_him = "the flowers are on their way"

import xmlrpclib
URI = "http://www.pythonchallenge.com/pc/phonebook.php"
pb = xmlrpclib.ServerProxy(URI)
print(pb.phone("Leopold")) # 555-VIOLIN

# http://www.pythonchallenge.com/pc/return/violin.html => "no! i mean yes! but ../stuff/violin.php."
# http://www.pythonchallenge.com/pc/stuff/violin.php
# TITLE: it's me. what do you want?

req = urllib2.Request(url='http://www.pythonchallenge.com/pc/stuff/violin.php',
                      headers={'Cookie': 'info=' + urllib.quote_plus(inform_him)})

f = urllib2.urlopen(req)
print f.read()

# "oh well, don't you dare to forget the balloons."

## import sys; sys.break("Stop!")
## import code; code.interact(local=locals())
