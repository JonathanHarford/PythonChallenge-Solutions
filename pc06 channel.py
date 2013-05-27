# http://www.pythonchallenge.com/pc/def/channel.html

from zipfile import ZipFile
from re import compile

nuffink = "90052.txt"
nuffink_re = compile("Next nothing is (\d+)")
z = ZipFile('pc06 channel.zip', 'r')
char_list = []

while True:

    with z.open(nuffink) as f:
        text = f.read()

    # print(text)

    char_list += z.getinfo(nuffink).comment
    try:
        nuffink = nuffink_re.findall(text)[0] + ".txt"
    except IndexError:
        break
        
print("".join(char_list))
