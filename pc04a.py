# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2,re
nuffink = "8022"
for i in range(1,200):
	f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nuffink)
	html = f.read()
	print(html)
	nuffink = re.findall("next nothing is (\d+)",html)[0]
	f.close()

