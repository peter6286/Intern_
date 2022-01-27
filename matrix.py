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







object = Solution()
#print(object.spiralOrder())
print(object.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))