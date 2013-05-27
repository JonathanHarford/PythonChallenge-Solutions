# http://www.pythonchallenge.com/pc/def/oxygen.html
# "smarty"
#
# Answers: http://www.pythonchallenge.com/pcc/def/integrity.html

## Well, this is useful:
# import code; code.interact(local=locals())
# sys.exit("BREAKY BREAK")
# from time import sleep

import Image

def ints2str(l):
    """Converts a list of integers to a string with chr."""
    return "".join([chr(n) for n in l])

im = Image.open("pc07 oxygen.png")

x = 0
l = []
p = im.getpixel((x,47))
while p[0] == p[1] == p[2]:
    l.append(p[0])
    x += 7
    p = im.getpixel((x,47))
text = ints2str(l)
print(text)
text = text[text.index("["):]
l = eval(text)
text = ints2str(l)
print(text)

# import code; code.interact(local=locals())
