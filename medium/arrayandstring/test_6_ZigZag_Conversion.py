"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

class Solution(object):
    def convert_1(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or not s or numRows >= len(s):
            return s
        lth = len(s)
        width = (-(-lth/numRows)) * (numRows-1)
        height = numRows
        record = [[''] * width for _ in range(height)]
        down = True
        i, j = 0, 0
        for c in s:
            record[i][j] = c
            if down and i == height - 1:
                down = False
            elif not down and i == 0:
                down = True
            if down:
                i += 1
            else:
                i -= 1
                j += 1
        rt = ''
        for line in record:
            rt += ''.join(line)
        return rt

    def convert_2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or numRows < 2 or len(s) <= numRows:
            return s
        record = [''] * numRows
        down = True
        i = 0
        for c in s:
            record[i] += c
            if down and i == numRows - 1:
                down = False
            elif not down and i == 0:
                down = True
            if down:
                i += 1
            else:
                i -= 1
        return ''.join(record)

