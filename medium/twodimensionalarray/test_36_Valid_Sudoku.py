"""
The Sudoku board could be partially filled, where empty cells are filled with the character '.'
"""
import collections

class Solution(object):
    def isValidSudoku_1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isValidBlock(row):
                return False
        for col in zip(*board):
            if not self.isValidBlock(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[a][b] for a in range(i, i+ 3) for b in range(j, j + 3)]
                if not self.isValidBlock(block):
                    return False
        return True

    def isValidBlock(self, string):

        valid = "123456789"
        s = [c for c in string if c != '.']
        return all(c in valid for c in s) and len(set(s)) == len(s)


    def isValidSudoku_2(self, board):
        a = [x for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i / 3, j / 3, c))]

        return 1 == max(collections.Counter(a).values() + [1])

    def isValidSudoku_3(self, board):

        ct = [x for i, row in enumerate(board) for j, c in enumerate(\
            row) if c != '.' for x in ((i, c), (j, c), (i / 3, j / 3, c))]
        return len(ct) == len(set(ct))



if __name__ == '__main__':
    s = Solution()
    board = [["9","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
    board2 = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
    rt1 = s.isValidSudoku_1(board)
    rt2 = s.isValidSudoku_2(board)

    rt3 = s.isValidSudoku_1(board2)
    rt4 = s.isValidSudoku_2(board2)
    rt5 = s.isValidSudoku_3(board)

    print rt1
    print rt2
    print rt3
    print rt4
    print rt5
