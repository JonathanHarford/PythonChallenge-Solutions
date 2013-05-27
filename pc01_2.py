from string import lowercase as cypher_in
from string import maketrans

# i hope you didnt translate it by hand. thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended. now apply on the url.

# jvvr://yyy.ravjqpejcnngpig.eqo/re/fgh/ocr.jvon
c1 = "http://www.pythonchallenge.com/pc/def/map.html"

# uvtkpi.ocmgvtcpu
c2 = "string.maketrans()"

cypher_out = cypher_in[2:] + cypher_in[:2]
translator = maketrans(cypher_in, cypher_out)
print(c1.translate(translator))
print(c2.translate(translator))
