"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

For 1-byte character, the first bit is a 0, followed by its unicode code.
For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.
This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.

Note:
The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

Example 1:

data = [197, 130, 1], which represents the octet sequence: 11000101 10000010 00000001.

Return true.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

data = [235, 140, 4], which represented the octet sequence: 11101011 10001100 00000100.

Return false.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
Seen this question in a real interview before?
Difficulty:Medium
Total Accepted:22.1K
Total Submissions:63.5K
Contributor:LeetCode
Subscribe to see which companies asked this question.

Related Topics

Python

1

"""


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        f0byte = int('0', 2)
        f1byte = int('10000000', 2)
        f2byte = int('11000000', 2)
        f3byte = int('11100000', 2)
        f4byte = int('11110000', 2)
        f5byte = int('11111000', 2)

        i = 0
        while i < len(data):
            if data[i] & f1byte == f0byte:
                i += 1
            elif data[i] & f3byte == f2byte:
                if i + 1 < len(data) and data[i + 1] & f2byte == f1byte:
                    i += 2
                else:
                    return False
            elif data[i] & f4byte == f3byte:
                if i + 2 < len(data) and data[i + 1] & f2byte == f1byte and data[i + 2] & f2byte == f1byte:
                    i += 3
                else:
                    return False
            elif data[i] & f5byte == f4byte:
                if i + 3 < len(data) and data[i + 1] & f2byte == f1byte and data[i + 2] & f2byte == f1byte and data[
                    i + 3] & f2byte == f1byte:
                    i += 4
                else:
                    return False
            else:
                return False
        return True


    def validUtf8_clean(self, data):
        need10 = 0

        f0byte = int('0', 2)
        f1byte = int('10000000', 2)
        f2byte = int('11000000', 2)
        f3byte = int('11100000', 2)
        f4byte = int('11110000', 2)
        f5byte = int('11111000', 2)

        for num in data:
            if need10 != 0:
                if num & f2byte != f1byte:
                    break
                need10 -= 1
            elif num & f3byte == f2byte:
                need10 = 1
            elif num & f4byte == f3byte:
                need10 = 2
            elif num & f5byte == f4byte:
                need10 = 3
            elif num & f1byte != f0byte:
                break
        else:
            if need10 == 0:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    data = [255]
    rt1 = s.validUtf8(data)
    rt2 = s.validUtf8_clean(data)

    print rt1
    print rt2