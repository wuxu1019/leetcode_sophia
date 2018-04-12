"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""

class Solution(object):
    def lengthLongestPath_hashmap(self, input):
        """
        :type input: str
        :rtype: int
        """
        l = input.split('\n')
        folder = {}
        rt = 0
        for i in range(len(l)):
            node = l[i]
            ct = 0
            while node[ct] == '\t':
                ct += 1
            if "." in node[ct:]:
                father = sum(folder[i]+1 for i in range(ct))
                rt = max(father+len(node[ct:]), rt)
            else:
                folder[ct] = len(node[ct:])
        return rt

    def lengthLongestPath_stack(self, input):
        l = input.split('\n')
        stk = []
        rt = 0
        for line in l:
            p = line.lstrip('\t')
            level = len(line) - len(p)
            while len(stk) > level:
                stk.pop()
            if '.' in line:
                rt = max(rt, sum(stk) + len(p))
            else:
                stk.append(len(p)+1)
        return rt


if __name__ == '__main__':
    s = Solution()
    path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    rt1 = s.lengthLongestPath_hashmap(path)
    rt3 = s.lengthLongestPath_stack(path)
    print rt1
    print rt3

    path = "5.txt"
    rt2 = s.lengthLongestPath_hashmap(path)
    rt4 = s.lengthLongestPath_stack(path)
    print rt2
    print rt4


