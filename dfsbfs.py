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
    # https://leetcode.com/problems/number-of-islands/


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
    # https://leetcode.com/problems/surrounded-regions/

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






    # 155. Min Stack
    # Input
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]
    #
    # Output
    # [null,null,null,null,-3,null,0,-2]
    # https://leetcode.com/problems/min-stack/


    class MinStack(object):

        def __init__(self):
            self.stack = []         #用两个stack来存放值
            self.minstack = []      # 一个存放原来的值一个存放当前点最小的值

        def push(self, val):
            self.stack.append(val)
            val = min(val,self.minstack[-1] if self.minstack else val) #比较取得当前最小的值
            self.minstack.append(val)
            """
            :type val: int
            :rtype: None
            """

        def pop(self):
            self.stack.pop()
            self.minstack.pop()
            """
            :rtype: None
            """

        def top(self):
            return self.stack[-1]

        def getMin(self):
            return self.minstack[-1]

    # 232. Implement Queue using Stacks
    # Input
    # ["MyQueue", "push", "push", "peek", "pop", "empty"]
    # [[], [1], [2], [], [], []]
    # Output
    # [null, null, null, 1, 1, false]
    # https://leetcode.com/problems/implement-queue-using-stacks/

    class myqueue(object):
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def push(self, x):
            self.stack1.append(x)
            """
            :type x: int
            :rtype: None
            """

        def pop(self):      #再加进去的时候就变换了顺序
            n = len(self.stack1)-1
            for i in range(n):
                self.stack2.append(self.stack1.pop())
            res = self.stack1.pop()
            for i in range(n):
                self.stack1.append(self.stack2.pop())
            return res


        def peek(self):
            n = len(self.stack1) - 1
            for i in range(n):
                self.stack2.append(self.stack1.pop())
            res = self.stack1[0]
            for i in range(n):
                self.stack1.append(self.stack2.pop())
            return res


        def empty(self):
            return (self.stack1) == 0




    class MyStack(object):
        def __init__(self):
            self.q1 = []
            self.q2 = []

        def push(self, x):
            self.q2.append(x)
            for i in range(len(self.q1)):
                self.q2.append(self.q1.pop(0))
            self.q1 = self.q2

        def pop(self):
            return self.q1.pop()

        def top(self):
            return self.q1[-1]


        def empty(self):
            return len(self.q1)==0

    def zigZag(self,arr, n):
        # Flag true indicates relation "<" is expected,
        # else ">" is expected. The first expected relation
        # is "<"
        flag = True
        count = 0
        for i in range(n - 1):
            # "<" relation expected
            if flag is True:
                # If we have a situation like A > B > C,
                # we get A > B < C
                # by swapping B and C
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    count +=1
                # ">" relation expected
            else:
                # If we have a situation like A < B < C,
                # we get A < C > B
                # by swapping B and C
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    count +=1
            flag = bool(1 - flag)
        print(arr)
        return count
















object = Solution()
print(object.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(object.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
arr = [2,1,2,3,4,5,2,9]
n = len(arr)
print(object.zigZag(arr, n))
print(15//2)

