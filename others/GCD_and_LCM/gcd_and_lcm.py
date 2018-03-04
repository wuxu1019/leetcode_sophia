
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x*y/gcd(x, y)


a, b = 1, 5
g, l = gcd(a, b), lcm(a, b)
print '{} and {}: gcd is {}, lcm {}'.format(a, b, g, l)
a, b = 2, 5
g, l = gcd(a, b), lcm(a, b)
print '{} and {}: gcd is {}, lcm {}'.format(a, b, g, l)
a, b = 4, 8
g, l = gcd(a, b), lcm(a, b)
print '{} and {}: gcd is {}, lcm {}'.format(a, b, g, l)
a, b = 4, 6
g, l = gcd(a, b), lcm(a, b)
print '{} and {}: gcd is {}, lcm {}'.format(a, b, g, l)
a, b = 0, 5
g, l = gcd(a, b), lcm(a, b)
print '{} and {}: gcd is {}, lcm {}'.format(a, b, g, l)

