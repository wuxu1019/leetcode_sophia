"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""
import re

class Solution(object):
    def decodeString_stk(self, s):
        """
        :type s: str
        :rtype: str
        """
        cur_str = ''
        num = 0
        stk = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stk.append(num)
                stk.append(cur_str)
                num = 0
                cur_str = ''
            elif c == ']':
                pre_str = stk.pop()
                pre_num = stk.pop()
                cur_str = pre_str + cur_str * pre_num
            else:
                cur_str += c
        return cur_str

    def decodeString_re(self, s):
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s


if __name__ == '__main__':
    s = Solution()
    l = 'a3[df4[r]]5[f]'
    rt1 = s.decodeString_re(l)
    print rt1

    rt2 = s.decodeString_stk(l)
    print rt2
