def sumDigital(s):
    count = 0
    for c in s:
        try:
            print "{} is a digital".format(c)
            count += int(c)
        except ValueError:
            print "{} is not a digital".format(c)
    return count

def findAnEven(l):
    for i in l:
        if not i&1:
            return i
    raise ValueError("l does not contatin an even number")

# test1
#s = raw_input('inter a string:  ')
#ct = sumDigital(s)
#print "{} to get {}".format(s, ct)

# test2
findAnEven([13, 3,3, 5])


