class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False
    def dfs(self, board, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found = (
            self.dfs(board, word, i + 1, j, index + 1)
            or self.dfs(board, word, i - 1, j, index + 1)
            or self.dfs(board, word, i, j + 1, index + 1)
            or self.dfs(board, word, i, j - 1, index + 1)
        )
        board[i][j] = temp
        return found