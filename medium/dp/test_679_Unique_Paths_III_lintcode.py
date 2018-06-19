"""
Description
Follow up for "Unique Paths II": http://lintcode.com/en/problem/unique-paths-ii/

Now each grid contains a value, so each path also has a value. Find the sum of all the unique values paths.

Have you met this question in a real interview?
Example
For example,

[
  [1,1,2],
  [1,2,3],
  [3,2,4]
]
There are 2 unique value path:
[1,1,2,3,4] = 11
[1,1,2,2,4] = 10

return 21
"""


class Solution:
    """
    @param: : an array of arrays
    @return: the sum of all unique weighted paths
    """

    def uniqueWeightedPaths(self, grid):
        # write your codes here
        R, C = len(grid), len(grid[0])
        if not R or not C:
            return 0
        record = [[grid[0][0]]]
        for i in range(1, C):
            record.append([grid[0][i] + record[i - 1][0]])

        for i in range(1, R):
            for j in range(C):
                if j == 0:
                    record[j] = [v + grid[i][j] for v in record[j]]
                else:
                    record[j] = [v + grid[i][j] for v in list(set(record[j - 1]) | set(record[j]))]

        return sum(record[-1])

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,2],[1,2,3],[3,2,4]]
    rt = s.uniqueWeightedPaths(grid)
    print rt