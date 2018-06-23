"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    def exist_n2_space(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        R, C = len(board), len(board[0])
        visited = [[False] * C for _ in range(R)]

        def existHelper(board, i, j, word, p):
            if visited[i][j]:
                return False
            if board[i][j] == word[p]:
                if p == len(word) - 1:
                    return True
                visited[i][j] = True
                for mv_i, mv_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i = i + mv_i
                    new_j = j + mv_j
                    if 0 <= new_i < R and 0 <= new_j < C and existHelper(board, new_i, new_j, word, p + 1):
                        return True
                visited[i][j] = False
            return False
x
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == word[0] and existHelper(board, i, j, word, 0):
                    return True
        return False


    def exist_no_space(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        R, C = len(board), len(board[0])

        def existHelper(board, i, j, word, p):
            if board[i][j] == word[p]:
                if p == len(word) - 1:
                    return True
                temp = board[i][j]
                board[i][j] = '#'
                for mv_i, mv_j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i = i + mv_i
                    new_j = j + mv_j
                    if 0 <= new_i < R and 0 <= new_j < C and existHelper(board, new_i, new_j, word, p + 1):
                        return True
                board[i][j] = temp
            return False

        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == word[0] and existHelper(board, i, j, word, 0):
                    return True
        return False