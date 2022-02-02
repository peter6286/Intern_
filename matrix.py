class Solution:
    # 48. Rotate Image
    # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [[7,4,1],[8,5,2],[9,6,3]]
    # Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    # https://leetcode.com/problems/rotate-image/

    def rotate(self, matrix):
        l,r = 0 ,len(matrix)-1
        while l < r :
            for i in range (r-l):
                top,bottom = l,r
                # save the topleft
                topleft = matrix[top][l+i]
                # move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]
                # move bottom right into bottom left
                matrix[bottom+i][l]=matrix[bottom][r-i]
                # move top right into bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                # move top left into top right
                matrix[top+i][r]=topleft
            l+=1
            r-=1

    # 54. Spiral Matrix
    # Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [1,2,3,6,9,8,7,4,5]
    # Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    # https://leetcode.com/problems/spiral-matrix/

    def spiralOrder(self, matrix):
        res = []
        top,bottom = 0,len(matrix)
        left,right = 0 ,len(matrix[0])
        while left < right and top < bottom:
            # get every i in the top row
            for i in range (left,right):
                res.append(matrix[top][i])
            top +=1
            # get every i in the right col
            for i in range (top,bottom):
                res.append(matrix[i][right-1])
            right -=1

            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom -1][i])
            bottom-=1
            # get every i in the left clo
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left +=1

        return res

    # 59. Spiral Matrix II
    # Input: n = 3
    # Output: [[1,2,3],[8,9,4],[7,6,5]]
    # Input: n = 1
    # Output: [[1]]
    # https://leetcode.com/problems/spiral-matrix-ii/

    def generateMatrix(self, n):
        if not n :
            return []
        res = [[0 for _ in range(n)] for _ in range (n)]
        left,right = 0,n-1
        top,bottom = 0,n-1
        num = 1

        while left <= right and top <= bottom:
            for i in range(left,right+1):
                res[top][i]=num
                num +=1
            top +=1

            for i in range(top,bottom+1):
                res[i][right] = num
                num +=1
            right -=1

            for i in range(right,left-1,-1):
                res[bottom][i]=num
                num+=1
            bottom -=1

            for i in range(bottom,top-1,-1):
                res[i][left] = num
                num+=1
            left +=1

            return res


    # 73. Set Matrix Zeroes
    # Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    # Output: [[1,0,1],[0,0,0],[1,0,1]]
    # Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    # https://leetcode.com/problems/set-matrix-zeroes/

    def setZeroes(self, matrix):
        row,col = len(matrix),len(matrix[0])
        rowzeros = False
        # determine which rows/cols need to be zero
        for r in range (row):
            for c in range(col):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        rowzeros=True

        #将中间的值填充好
        for r in range(1,row):
            for c in range (1,col):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        # 将边缘的也填充好
        if matrix[0][0]==0:
            for r in range (row):
                matrix[r][0]=0
        if rowzeros:
            for c in range(col):
                matrix[0][c]=0

        return matrix


    # 378. Kth Smallest Element in a Sorted Matrix
    # Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    # Output: 13
    # Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15],
    # and the 8th smallest number is 13
    # Input: matrix = [[-5]], k = 1
    # Output: -5
    # https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

    def kthSmallest(self, matrix, k):
        row,col = len(matrix),len(matrix[0])
        templist=[]
        for r in range(row):
            for c in range(col):
                templist.append(matrix[r][c])
        templist.sort()
        print(templist)
        return templist[k-1]


    # 74. Search a 2D Matrix
    # Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    # Output: true
    # Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
    # Output: false
   # https://leetcode.com/problems/search-a-2d-matrix/

    def searchMatrix(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        for r in range(row ):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        return False



    # 240. Search a 2D Matrix II
    # Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
    # target = 5
    # Output: true
    # Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
    # target = 20
    # Output: false

    def searchMatrix2(self, matrix, target):
        if not len(matrix) or not len (matrix[0]):
            return False
        h,w = len(matrix),len(matrix[0])

        for row in matrix:
            if row[0]<=target<=row[-1]: #先锁定可能在的row
                left,right = 0,w-1

                while left <= right:        #再使用biany search 找
                    mid = (left+right)//2
                    mid_value = row[mid]
                    if target > mid_value:
                        left = mid + 1
                    elif target < mid_value:
                        right = mid -1
                    else:
                        return True         #在row里找不到也会进入下一个row用for loop
        return False


    # 79. Word Search
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    # Output: true
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
    # Output: true
    # Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
    # Output: false


    def exist(self, board, word):
        rows,cols = len(board),len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):      # 如果到了最后一位有一样的
                return True
            if (r<0 or c<0 or r>=rows or c >= cols
            or word[i] != board[r][c] or (r,c) in path):       #是false的所有情况
                return False

            path.add((r,c))         #将有效的加入path中
            res = (dfs(r+1,c,i+1)or
                   dfs(r-1,c,i+1)or
                   dfs(r,c+1,i+1)or
                   dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False


    # 36. Valid Sudoku
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)     #为三个条件形成三个set
        rows = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":        #如果是.就跳过
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r//3,c//3)]): #除三后刚好分为9个小方块形成9个set
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return Ture











object = Solution()
#print(object.spiralOrder())
print(object.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(object.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
print(object.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
print(object.searchMatrix2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
print(object.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))