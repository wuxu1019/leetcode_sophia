"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        ct_R = ct_L = 0
        sub_s, sub_e = '', ''
        for i in range(len(start)):
            if start[i] == 'R':
                ct_R += 1
                sub_s += 'R'
            if end[i] == 'R':
                ct_R -= 1
                sub_e += 'R'
            if end[i] == 'L':
                ct_L += 1
                sub_e += 'L'
            if start[i] == 'L':
                ct_L -= 1
                sub_s += 'L'
            if ct_R < 0 or ct_L < 0:
                return False
        return ct_R == 0 and ct_L == 0 and sub_s == sub_e