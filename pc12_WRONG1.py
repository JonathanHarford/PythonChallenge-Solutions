# http://www.pythonchallenge.com/pc/return/evil.html
# ANSWER:
#
# TITLE: dealing evil
#
# This first attempt of a solution is based on the fact that the image looks
# like it can be "unshuffled" in a similar manner to the last one into twelve
# images. It can, but you just end up with twelve similar color-shifted images.


from PIL import Image

im = Image.open("pc12 evil1.jpg")
w,h = im.size
ims = [
        [
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6))
        ],
        [
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6)),
            Image.new("RGB",(w/2,h/6))
        ]
]
print(ims)

for x in range(w):
  for y in range(h):
    (sm_x,sm_y) = (x // 2,y // 6)
    p = im.getpixel((x,y))
    print("Putting pixel {0} with color {1} into image {2} at {3}.".format(
        (x,y),
        p,
        str(x%2)+str(y%6),
        (x // 2, y // 6)
    ))
    ims[x%2][y%6].putpixel((sm_x,sm_y),p)

ims[0][0].save("00.png","png")
ims[0][1].save("01.png","png")
ims[0][2].save("02.png","png")
ims[0][3].save("03.png","png")
ims[0][4].save("04.png","png")
ims[0][5].save("05.png","png")
ims[0][0].save("00.png","png")
ims[1][1].save("11.png","png")
ims[1][2].save("12.png","png")
ims[1][3].save("13.png","png")
ims[1][4].save("14.png","png")
ims[1][5].save("15.png","png")