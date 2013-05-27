# http://huge:file@www.pythonchallenge.com/pc/return/italy.html
#
# ANSWER: http://www.pythonchallenge.com/pcc/return/uzi.html
#
# TITLE: walk around
# remember: 100*100 = (100+99+99+98) + (...

# Well 100*100 = (100+99+99+98+98+...+1+1), which is to say:
# 100*100 == sum([i//2 for i in range(200,0,-1)])

# After much attemptage, it seems to me
# I need to make a spiral out of this wire.
# #####
#     #
# ### #
# #   #
# #####
import Image, ImageDraw

# Open image and convert to a list of pixels.
im = Image.open("pc14 wire.png")
pix_list = [im.getpixel((x,0)) for x in range(im.size[0])]

im2 = Image.new("RGB",(102,102))

# This code reveals the word "bit", whose page just says:
# "you took the wrong curve."
## for x in range(im.size[0]):
##   im2.putpixel((x%100,x//100),im.getpixel((x,0)))

draw = ImageDraw.Draw(im2)
draw.rectangle((0,0,101,101), outline=(255,0,255), fill=(0,0,0))


pos = [1,1]
directions = ((1,0),(0,-1),(-1,0),(0,1))
d = 0
while pix_list:
    print(pos)
    if im2.getpixel(tuple(pos)) <> (0,0,0):
        print(im2.getpixel(tuple(pos)))
        print("Turning")
        pos[0] += -directions[d%4][0]
        pos[1] += -directions[d%4][1]
        d += 1
        pos[0] += directions[d%4][0]
        pos[1] += directions[d%4][1]

    else:
        im2.putpixel(pos, pix_list.pop(0))
        pos[0] += directions[d%4][0]
        pos[1] += directions[d%4][1]

im2.show()

# import code; code.interact(local=locals())
