"""
give two string, to present two integers
sum the two integers
return string
"""



def twoSum(a, b):
    la, lb = len(a), len(b)
    if la > lb:
        b = '0'*(la-lb) + b
    else:
        a = '0'*(lb-la) + a
    a, b = list(a), list(b)
    rt = []
    carry = 0
    for i in range(la-1, -1, -1):
        c = int(a[i]) + int(b[i]) + carry
        if c >= 10:
            carry = 1
            c = c % 10
        else:
            carry = 0
        rt.append(str(c))
    if carry:
        rt.append('1')
    return ''.join(rt[::-1])


    
a = '12345112'
b = '8984329'

c = twoSum(a, b)
print c
