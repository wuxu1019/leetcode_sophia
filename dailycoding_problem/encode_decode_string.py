"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""
import itertools


def encode(s):

    rt = ''
    for k, v in itertools.groupby(s):

        rt += str(len(list(v)))
        rt += k
    return rt

def decode(s):

    rt = ''
    times = 0
    for c in s:
        if c.isalpha():
            rt += c * times
            times = 0
        else:
            times = times * 10 + int(c)
    return rt


if __name__ == '__main__':
    s = 'AAAABBBCCDAAAAAAAAAAAAA'
    rt = encode(s)
    if rt == "4A3B2C1D13A":
        print True
    else:
        print False

    s = "4A3B2C1D13A"
    rt = decode(s)

    if rt == 'AAAABBBCCDAAAAAAAAAAAAA':
        print True
    else:
        print False