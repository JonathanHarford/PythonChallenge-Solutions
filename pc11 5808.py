# http://www.pythonchallenge.com/pc/return/5808.html
#
# ANSWER: http://huge:file@www.pythonchallenge.com/pc/return/evil.html


import Image
im = Image.open("pc11 cave.jpg")
for x in range(im.size[0]):
    for y in range(im.size[1]):
        im.putpixel((x//2, y//2), im.getpixel((x, y)))
im.show()