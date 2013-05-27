# http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
#
# ANSWER: http://www.pythonchallenge.com/pcc/return/italy.html
#
# TITLE: call him
# phone that <remote /> evil

# link on JKL5 leads to phonebook.php

##>>> pb.system.listMethods()
##['phone',
## 'system.listMethods',
## 'system.methodHelp',
## 'system.methodSignature',
## 'system.multicall',
## 'system.getCapabilities']
##
##>>> pb.system.methodHelp("phone")
##'Returns the phone of a person'
##
##>>> pb.phone(str)
##'He is not the evil.'

import xmlrpclib

URI = "http://www.pythonchallenge.com/pc/phonebook.php"
pb = xmlrpclib.ServerProxy(URI)
print(pb.phone("Bert"))