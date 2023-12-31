from typing import List
# https://leetcode.com/problems/word-search/
# not so optimized, clumsy
def exist(board: List[List[str]], word: str) -> bool:
    m = len(board) # row
    n = len(board[0]) # col
    v = [[0] * n for _ in range(m)]
    found = False
    def search(row, col, index):
        nonlocal found
        if board[row][col] != word[index] or found:
            return
        if index == len(word) - 1:
            found = True
            return
        if row > 0 and v[row - 1][col] == 0:
            v[row - 1][col] = 1 
            search(row - 1, col, index + 1)
            v[row - 1][col] = 0 # annoying, we need to release the visited point if that is not a solution
        if row < m - 1 and v[row + 1][col] == 0:
            v[row + 1][col] = 1
            search(row + 1, col, index + 1)
            v[row + 1][col] = 0
        if col > 0 and v[row][col - 1] == 0:
            v[row][col - 1] = 1
            search(row, col - 1, index + 1)
            v[row][col - 1] = 0
        if col < n - 1 and v[row][col + 1] == 0:
            v[row][col + 1] = 1
            search(row, col + 1, index + 1)
            v[row][col + 1] = 0
    for i in range(m):
        for j in range(n):
            v = [[0] * n for _ in range(m)]
            v[i][j] = 1
            search(i, j, 0)
            if found:
                return True
    return False
# exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
# exist([["a","b"],["c","d"]], "cdba")
# exist([["a","a"]], "aaa")

# https://leetcode.com/problems/number-of-islands/
def numIslands(grid: List[List[str]]) -> int:
    n = len(grid) # row
    m = len(grid[0]) # col
    def dfs(row, col):
        if grid[row][col] == "1":
            grid[row][col] = "*"
        else:
            return
        if row > 0:
            dfs(row - 1, col)
        if row < n - 1:
            dfs(row + 1, col)
        if col > 0:
            dfs(row, col - 1)
        if col < m - 1:
            dfs(row, col + 1)
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                dfs(i, j)
                ans += 1
    return ans
