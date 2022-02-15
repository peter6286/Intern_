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


    # 225. Implement Stack using Queues
    # Input
    # ["MyStack", "push", "push", "top", "pop", "empty"]
    # [[], [1], [2], [], [], []]
    # Output
    # [null, null, null, 2, 2, false]

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


    # 150. Evaluate Reverse Polish Notation
    # Input: tokens = ["2","1","+","3","*"]
    # Output: 9
    # Explanation: ((2 + 1) * 3) = 9
    # Input: tokens = ["4","13","5","/","+"]
    # Output: 6
    # Explanation: (4 + (13 / 5)) = 6

    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                else:
                    stack.append(int(float(l) / r))
        return stack.pop()

    # 71. Simplify Path
    # Input: path = "/home/"
    # Output: "/home"
    # Explanation: Note that there is no trailing slash after the last directory name.

    def simplifyPath(self, path):
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":            #用\来进行dictory分层所以结尾的时候得加"\"
                if cur == "..":     #如果curr里只有两个dot说明回到上层dict 需要用pop
                    if stack:stack.pop()
                    elif cur != "" and cur!=".":   #除了特殊情况外都将curr压入stack中
                        stack.append(cur)
                    cur =""         #清空stack
            else:
                cur += c
        return "/" + "/".join(stack)        #用join操作连接所有东西在一起


    # 388. Longest Absolute File Path
    # Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    # Output: 20
    # Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
    # Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    # Output: 32

    def lengthLongestPath(self, s) :
        paths, stack, ans = s.split('\n'), [], 0
        for path in paths:
            p = path.split('\t')            #用切割\t来识别现在的深度
            depth, name = len(p) - 1, p[-1]
            l = len(name)
            while stack and stack[-1][1] >= depth:  #如果之前的深度比现在遍历的深返回同一级上继续遍历
                stack.pop()
            if not stack:
                stack.append((l, depth))    # stack [current total length][depth of the path]
            else:
                stack.append((l + stack[-1][0], depth))     #现在path的长度和深度放进stack中
            if '.' in name: ans = max(ans, stack[-1][0] + stack[-1][1])
        return ans


    # 394. Decode String
    # Input: s = "3[a]2[bc]"
    # Output: "aaabcbc"c
    # Input: s = "3[a2[c]]"
    # Output: "accaccacc"
    # Input: s = "2[abc]3[cd]ef"
    # Output: "abcabccdcdcdef"
    # https://leetcode.com/problems/decode-string/

    def decodeString(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] !="]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "]":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*substr)

        return "".join(stack)

    def calculate(self, s):
        num = 0
        pre_op = '+'
        s += '+'
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append((operant * num))
                elif pre_op == '/':
                    operant = stack.pop()
                    stack.append(math.trunc(operant / num))
                num = 0
                pre_op = c
        return sum(stack)


























object = Solution()

#print(object.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
arr = [2,1,2,3,4,5,2,9]
n = len(arr)
#print(object.zigZag(arr, n))
print(15//2)
print(object.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(object.calculate("3+2*2"))
