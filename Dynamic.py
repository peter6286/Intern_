class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            tempsum = curSum + num   #到这个点为止最优的所有index的合
            curSum = max(num, tempsum) #比较是加上num后大（有负数）还是原本数字大。取value大的为新的current
            maxSum = max(maxSum, curSum) #更新最优的总数

        return maxSum


    # 70. Climbing Stairs
    # Input: n = 2
    # Output: 2
    # Explanation: There are two ways to climb to the top.
    # 1. 1 step + 1 step
    # 2. 2 steps
    #  Input: n = 3
    # Output: 3
    # Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step


    def climbStairs(self, n, d={1: 1, 2: 2}):
        if n == 0:
            return 0
        if n not in d:
            d[n] = self.climbStairs(n - 1, d) + self.climbStairs(n - 2, d) #dictionary里只有1和2
        return d[n] #按值返回

    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while (j < len(t) and i < len(s)):
            if (s[i] == t[j]):
                i += 1
                j += 1
            else:
                j += 1
        if (i == len(s)):
            return True
        return False


    # 62. Unique Paths
    # Input: m = 3, n = 2
    # Output: 3
    # Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    # 1. Right -> Down -> Down
    # 2. Down -> Down -> Right
    # 3. Down -> Right -> Down


    def uniquePaths(self, m, n): # n为x轴 m为y轴
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for c in range(n):
            dp[0][c] = 1

        for r in range(m):
            dp[r][0] = 1

        for r in range(1,m):
            for c in range(1,n):
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]


    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]


    # 63. Unique Paths II
    # Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    # Output: 2
    # Explanation: There is one obstacle in the middle of the 3x3 grid above.
    # There are two ways to reach the bottom-right corner:
    # 1. Right -> Right -> Down -> Down
    # 2. Down -> Down -> Right -> Right


    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for c in range(n):
            if obstacleGrid[0][c] == 1: break
            dp[0][c] = 1

        for r in range(m):
            if obstacleGrid[r][0] == 1: break
            dp[r][0] = 1

        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c]== 1:
                    dp[r][c]=0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[-1][-1]


    # 120. Triangle
    # Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    # Output: 11
    # Explanation: The triangle looks like:
    #    2
    #   3 4
    #  6 5 7
    # 4 1 8 3
    # The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).


    def minimumTotal(self, triangle):
        dp = [0]*(len(triangle)+1)

        for row in triangle[::-1]:  #倒转过来从底下开始
            for i,n in enumerate(row):  #访问index和item。因为是三角形长度会越来越短
                dp[i] = n + min(dp[i],dp[i+1])  #当前的点的值加上最小的

        return dp[0]

    # 279. Perfect Squares
    # Input: n = 12
    # Output: 3
    # Explanation: 12 = 4 + 4 + 4.
    # Input: n = 13
    # Output: 2
    # Explanation: 13 = 4 + 9.

    def numSquares(self, n):
        dp = [n] * (n+1)
        dp[0] = 0
        for target in range(1,n+1):  # 从1开始一直算到target上
            for s in range (1,target+1):
                square = s*s    # square
                if target - square < 0: # 如果小于0停止
                    break
                dp[target]=min(dp[target],1+dp[target-square])
        return dp[n]    #做coin changed problem



a= [-2,1,-3,4,-1,2,1,-5,4]
object = Solution()
print(object.maxSubArray(a))
print(object.climbStairs(5))
print(object.isSubsequence("abc","ahbgdc"))
print(object.uniquePaths(3,7))
print(object.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(object.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(object.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(object.numSquares(12))