"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        mlth = max(len(version1), len(version2))
        sec1 = sec2 = 0
        i = j = 0
        while i < mlth and j < mlth:
            while i < len(version1) and version1[i] != '.':
                sec1 = 10 * sec1 + int(version1[i])
                i += 1
            while j < len(version2) and version2[j] != '.':
                sec2 = 10 * sec2 + int(version2[j])
                j += 1
            if sec1 < sec2:
                return -1
            elif sec1 > sec2:
                return 1
            else:
                i += 1
                j += 1
                sec1 = sec2 = 0
        return 0

