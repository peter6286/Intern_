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
            d[n] = self.climbStairs(n - 1, d) + self.climbStairs(n - 2, d)
        return d[n]

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

    def uniquePaths(self, m, n): # n为x轴 m为y轴
        dp = [[1] * m for z in range(n)]  #初始化

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  #往dp里填充value
        return dp[-1][-1]       #返回list的最后一个就是grid里的右下

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


a= [-2,1,-3,4,-1,2,1,-5,4]
object = Solution()
print(object.maxSubArray(a))
print(object.climbStairs(5))
print(object.isSubsequence("abc","ahbgdc"))
print(object.uniquePaths(3,2))
print(object.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))