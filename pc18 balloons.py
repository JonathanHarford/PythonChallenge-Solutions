# http://huge:file@www.pythonchallenge.com/pc/return/balloons.html
# ANSWER:
# TITLE: can you tell the difference?

# http://www.pythonchallenge.com/pc/return/brightness.html
# "maybe consider deltas.gz" which contains deltas.txt

def hex2chr(h):
    try:
        return chr(int(h, 16))
    except ValueError:
        return ""

d1 = []
d2 = []

with open("pc18 delta.txt") as f:
    for row in f.readlines():
        d1 += row[:53].split(" ")
        d2 += row[:56].split(" ")

img1 = "".join([hex2chr(h) for h in d1])
img2 = "".join([hex2chr(h) for h in d2])

with open("img1.png","w") as f:
    f.write(img1)

with open("img2.png","w") as f:
    f.write(img2)

## import sys; sys.exit("Stop!")
## import code; code.interact(local=locals())
