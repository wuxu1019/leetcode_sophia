"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution(object):
    def multiply_1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        zeros = 0
        rt = '0'
        for i in num2:
            carry = 0
            base = ''
            if i == 0:
                base = 0
            else:
                for j in num1:
                    carry, res = divmod(int(i) * int(j) + carry, 10)
                    base += str(res)
                if carry:
                    base += str(carry)
                base = '0' * zeros + base

            p = 0
            lth = max(len(base), len(rt))
            carry = 0
            add = ''
            while p < lth:
                a = int(base[p]) if p < len(base) else 0
                b = int(rt[p]) if p < len(rt) else 0
                carry, c = divmod(a + b + carry, 10)
                add += str(c)
                p += 1
            if carry:
                add += str(carry)
            rt = add
            zeros += 1

        rt = rt[::-1].lstrip('0')
        return '0' if not rt else rt

    def multiply_2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = [int(i) for i in num1[::-1]]
        num2 = [int(i) for i in num2[::-1]]
        l1, l2 = len(num1), len(num2)

        ans = [0] * (l1 + l2)
        for i in range(l1):
            for j in range(l2):
                ans[i + j] += num1[i] * num2[j]
                ans[i + j + 1] += ans[i + j] / 10
                ans[i + j] = ans[i + j] % 10
        return ''.join(str(i) for i in ans[::-1]).lstrip('0')