"""
compare if two strings with backslash are the same
backslash means delete the front character
"""

def compare(str1, str2):
    p1, p2 = len(str1)-1, len(str2)-1
    while p1 >=0 and p2 >=0:
	ct1, ct2 = 0, 0
        p = p1
        while p >= 0 and str1[p] == '\\':
            p, ct1 = p-1, ct1+2
        p = p2
        while p >= 0 and str2[p] == '\\':
            p, ct2 = p-1, ct2+2
        p1, p2 = p1-ct1, p2-ct2
        if p1 < 0 and p2 < 0:
            return True
        if p1 < 0 or p2 < 0:
            return False
        if str1[p1] == str2[p2]:
            p1, p2 = p1-1, p2-1
        else:
            return False

    return True
   
           
str1 = 'a\\bc\\def\\ghjkl\\\\f'
str2 = 'bdeghjf'
rt = compare(str1, str2)
print "compare {0} and {1} is same: {2}".format(str1, str2, rt)

str1 = 'a\\bc\\def\\ghjkl\\\\f'
str2 = 'abdeghjf'
rt = compare(str1, str2)
print "compare {0} and {1} is same: {2}".format(str1, str2, rt)

str1 = 'a\\bc\\def\\ghjkl\\\\f'
str2 = '\\\\\\bdeghjf'
rt = compare(str1, str2)
print "compare {0} and {1} is same: {2}".format(str1, str2, rt)
