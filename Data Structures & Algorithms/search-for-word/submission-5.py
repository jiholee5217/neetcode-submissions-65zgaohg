class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, word, r, c, 0):
                    return True
        return False

    def dfs(self, board, word, r, c, index):
        if index == len(word):
            return True
        if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[index] != board[r][c]):
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (
            self.dfs(board, word, r + 1, c, index + 1) or
            self.dfs(board, word, r - 1, c, index + 1) or
            self.dfs(board, word, r, c + 1, index + 1) or
            self.dfs(board, word, r, c - 1, index + 1)
        )
        board[r][c] = temp
        return found