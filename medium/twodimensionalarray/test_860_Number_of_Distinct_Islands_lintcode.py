"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Notice that:

11
1
and

 1
11
are considered different island shapes, because we do not consider reflection / rotation.


"""
import collections
class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """

    def numberofDistinctIslands(self, grid):
        # write your code here
        R, C = len(grid), len(grid[0])
        mp = collections.Counter()
        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    island = self.findIslands(i, j, R, C, grid)
                    mp_key = []
                    for p in range(len(island)):
                        if p == 0:
                            mp_key.append((0, 0))
                        else:
                            mp_key.append((island[p][0] - island[p - 1][0], island[p][1] - island[p - 1][1]))
                    mp[tuple(mp_key)] += 1
        return len(mp)

    def findIslands(self, i, j, R, C, grid):
        grid[i][j] = 0
        rt = [[i, j]]
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i_mv = i + di
            j_mv = j + dj
            if 0 <= i_mv < R and 0 <= j_mv < C and grid[i_mv][j_mv]:
                rt += self.findIslands(i_mv, j_mv, R, C, grid)
        return rt

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,0,0,1],[1,0,0,0,0],[1,1,0,0,1],[0,1,0,1,1]]
    rt = s.numberofDistinctIslands(grid)
    print rt