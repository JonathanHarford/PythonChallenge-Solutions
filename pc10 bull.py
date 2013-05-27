# http://www.pythonchallenge.com/pc/def/bull.html
# ANSWER: http://www.pythonchallenge.com/pcc/return/5808.html
#
# TITLE: what are you looking at?
#
# a = [1, 11, 21, 1211, 111221,
# len(a[30]) = ?

# 1
# One 1
# 11
# Two 1
# 21
# One 2, One 1
# 1211
# ...
print "Python 2, right?"

def list2int(l):
    return int("".join(l))

def describer(l):

    # Convert input to a list
    if type(l) <> list:
        l = list(str(l))

    # ['1','1','2'] => ['1','1','1','1','1','3']

    nums = [1 for x in l]

    # print(l)
    # print(nums)

    i = 1
    while i < len(l):
        while l[i-1] == l[i]:
            l.pop(i)
            nums.pop(i)
            nums[i-1] += 1
            if i >= len(l): break
        i += 1

    r = []
    for i in range(len(l)):
        r.append(str(nums[i]))
        r.append(l[i])

    r = "".join(r)
    return r

i = 0
d = '1'
while i <= 30:
    print("i == {0}".format(i))
    print("a[{0}] == {1}".format(i,d))
    print("len(a[{0}]) == {1}".format(i,len(d)))
    d = describer(d)
    i += 1
