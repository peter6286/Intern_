class Solution:

    # 200. Number of Islands
    # Input: grid = [
    #   ["1","1","1","1","0"],
    #   ["1","1","0","1","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","0","0","0"]
    # ]
    # Output: 1
    # Input: grid = [
    #   ["1","1","0","0","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","1","0","0"],
    #   ["0","0","0","1","1"]
    # ]
    # Output: 3
    def numIslands(self, grid):
        if not grid:
            return 0
        rows ,cols = len(grid),len(grid[0])
        visit = set()
        island = 0

        def bfs(r,c):
            q = []
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.pop(0)
                direction = [[1,0],[-1,0],[0,1],[0,-1]] #在四个方向找
                for dr,dc in direction:
                    r,c = row+dr,col+dc
                    if ( r in range (rows) and          #在bfs中找连续是1的点然后加入queue和visit当中
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r,c ) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:      # 找到有"1"的点后做bfs，如果当前的点没有被visited过
                    bfs(r,c)
                    island+=1

        return island



    # 130. Surrounded Regions
    # Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]


    def solve(self, board):
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1 capture unsurrounded region (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                        (r in [0, ROWS - 1] or c in [0, COLS - 1])):
                    capture(r, c)

        # 2 capture surrounded region (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3 uncapture unsurrounded region (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

        return board


object = Solution()
print(object.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(object.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))


