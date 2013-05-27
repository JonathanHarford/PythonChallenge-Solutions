http://www.pythonchallenge.com/pc/def/map.html

from string import lowercase as cypher_in
from string import maketrans

coded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
cypher_out = cypher_in[2:] + cypher_in[:2]
translator = maketrans(cypher_in, cypher_out)
print(coded.translate(translator))
