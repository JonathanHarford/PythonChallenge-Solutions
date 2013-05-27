# http://huge:file@www.pythonchallenge.com/pc/return/mozart.html
#
# ANSWER: http://www.pythonchallenge.com/pcc/return/romance.html
#
# TITLE: let me get this straight

import Image

src = Image.open("pc16 mozart.gif")
dst = Image.open("pc16 mozart.gif")
src_list = [[src.getpixel((x,y)) for x in range(src.size[0])]
                                 for y in range(src.size[1])]
for y in range(src.size[1]):
    row = src_list[y]
    src_list[y] = row[row.index(195):] + row[:row.index(195)]
    for x in range(src.size[0]):
        dst.putpixel((x,y),src_list[y][x])

dst.show()

# import sys; sys.break("Stop!")
# import code; code.interact(local=locals())
