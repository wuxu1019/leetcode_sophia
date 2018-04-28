"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""


class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        if not matrix or not matrix[0]:
            return ans

        lr, lc = len(matrix), len(matrix[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def Pacific(mat):
            visited = set()
            for j in range(lc):
                dfs(mat, 0, j, visited)

            for i in range(lr):
                dfs(mat, i, 0, visited)
            return visited

        def Atlantic(mat):
            visited = set()
            for j in range(lc):
                dfs(mat, lr-1, j, visited)
            for i in range(lr):
                dfs(mat, i, lc-1, visited)
            return visited

        def dfs(mat, i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for dx, dy in direction:
                i_n = i + dx
                j_n = j + dy
                if 0 <= i_n < lr and 0 <= j_n < lc and mat[i_n][j_n] >= mat[i][j]:
                    dfs(mat, i_n, j_n, visited)

        v_p = Pacific(matrix)
        v_a = Atlantic(matrix)

        return [list(i) for i in v_p & v_a]



if __name__ == '__main__':
    s = Solution()
    ml = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    rt = s.pacificAtlantic(ml)
    print rt