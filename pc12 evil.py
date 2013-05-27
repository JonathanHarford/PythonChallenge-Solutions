# http://huge:file@www.pythonchallenge.com/pc/return/evil.html
# and
# http://www.pythonchallenge.com/pc/return/evil2.gfx
# ANSWER: http://www.pythonchallenge.com/pcc/return/disproportional.html
#
# TITLE: dealing evil
#
# disproportionality?


# Read the file in to a string, which we immediately turn into a list
s = open("pc12 evil2.gfx","rb").read()

for i in range(5):
    open("image"+str(i)+".jpg", "wb").write(s[i::5])

