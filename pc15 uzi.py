# http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
#
# ANSWER: http://www.pythonchallenge.com/pcc/return/mozart.html
#
# TITLE: whom?
# he ain't the youngest, he is the second
# todo: buy flowers for tomorrow

# PICTURE: Calendar Monday, January 26th, 1##6 (a leap year)

from calendar import isleap, weekday

# List years after Gregorian Reform (1582 - invention of the leap day) that:
# A. Start with a 1 (so before 2000)
# B. are leap years
# C. end with a "6"
# D. Have January 26 on a Monday

print([year for year in range(1586,2000,10)
                    if isleap(year) and weekday(year,1,26) == 0])


# possible_years = [1756, 1976]

# Well, Mozart was born on January 27, 1756...

## import code; code.interact(local=locals())
