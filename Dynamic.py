class Solution:
    # 53. Maximum Subarray
    # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.
    # Input: nums = [1]
    # Output: 1
    # Input: nums = [5,4,-1,7,8]
    # Output: 23
    # https://leetcode.com/problems/maximum-subarray/
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


    # 392. Is Subsequence
    # https://leetcode.com/problems/is-subsequence/


    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while (j < len(t) and i < len(s)):
            if (s[i] == t[j]):      #如果找到了i和j一块移动
                i += 1
                j += 1
            else:
                j += 1          # 没有找到的情况下只移动j
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


    # 64. Minimum Path Sum
    # Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
    # Output: 7
    # Input: grid = [[1,2,3],[4,5,6]]
    # Output: 12
    # https://leetcode.com/problems/minimum-path-sum/

    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        for c in range(1, n):       # 因为只能向下或往右将边缘的路径算好
            grid[0][c] += grid[0][c - 1]

        for r in range(1, m):
            grid[r][0] += grid[r - 1][0]

        for r in range(1, m):
            for c in range(1, n):       # 将中间的填充好是上面或者右边过来
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
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


    # 139. Word Break
    # Input: s = "leetcode", wordDict = ["leet","code"]
    # Output: true
    # Input: s = "applepenapple", wordDict = ["apple","pen"]
    # Output: true
    # Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    # Output: false
    # https://leetcode.com/problems/word-break/



    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[len(s)] = True   #最后一个肯定是true
        for i in range (len(s),-1,-1):  #倒序
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w : #构造的长度得小于s的长度同时substring得等于w
                    dp[i] = dp[i+len(w)]  #将这个点开始的设置为true利用加长度
                if dp[i]:   #不需要再找别的word
                    break
        return dp[0]


    # 322. Coin Change
    # Input: coins = [1,2,5], amount = 11
    # Output: 3
    # Input: coins = [2], amount = 3
    # Output: -1
    def coinChange(self, coins, amount):
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for a in range(1,amount+1):
            for c in coins:         #遍历所有的硬币的大小
                if a - c >= 0:      #如果是大于0可能就是一种接法
                    dp[a] = min(dp[a],1+dp[a-c])    #更新最优解
        return dp[amount] if dp[amount]!= amount + 1 else -1

    # 72. Edit Distance
    # Given two strings word1 and word2, return the minimum number of
    # operations required to convert word1 to word2.
    # You have the following three operations permitted on a word:
    #
    # Insert a character
    # Delete a character
    # Replace a character

    # Input: word1 = "horse", word2 = "ros"
    # Output: 3
    # Explanation:
    # horse -> rorse (replace 'h' with 'r')
    # rorse -> rose (remove 'r')
    # rose -> ros (remove 'e')

    # https://leetcode.com/problems/edit-distance/



    def minDistance(self, word1, word2):
        dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]

        for c in range(len(word2)+1):
            dp[len(word1)][c] = len(word2) - c   #word1 = ""是空的到word2的距离就是加多少个词

        for r in range(len(word1)+1):
            dp[r][len(word2)] = len(word1) - r  #word2 = ""是空的到word1的距离就是加多少个词

        for r in range(len(word1)-1,-1,-1):
            for c in range(len(word2)-1,-1,-1):
                if word1[r] == word2[c]:        #如果两个值相同
                    dp[r][c] = dp[r+1][c+1]
                else:     # 1 more step   delete    insert     replace
                    dp[r][c] = 1+ min(dp[r+1][c],dp[r][c+1],dp[r+1][c+1])

        return dp[0][0]


    # 97. Interleaving String
    # Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    # Output: true
    # Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    # Output: false
    # https://leetcode.com/problems/interleaving-string/
    def isInterleave(self, s1, s2, s3):
        dp = [[False]*(len(s2)+1) for _ in range (len(s1)+1)]
        dp[len(s1)][len(s2)]=True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]: # 检查s1往下一个词是否match
                    dp[i][j] = True
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]: # 检查s2往下一个词是否match
                    dp[i][j] = True
        return dp[0][0]


    # 221. Maximal Square
    # Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
    #                   ["1","1","1","1","1"],["1","0","0","1","0"]]
    # Output: 4
    # Input: matrix = [["0","1"],["1","0"]]
    # Output: 1
    # Input: matrix = [["0"]]
    # Output: 0
    # https://leetcode.com/problems/maximal-square/


    def maximalSquare(self, matrix):
        maxsquare = 0
        if not matrix:
            return maxsquare
        dp = matrix
        for c in range(len(matrix[0])):     #填充行和列没区别和原本的一样
            dp[0][c]= int(matrix[0][c])

        for r in range(len(matrix)):
            dp[r][0] = int(matrix[r][0])


        for r in range(1,len(matrix)):
            for c in range (1,len(matrix[0])):
                if r>0 and c>0 :#保护edge case
                    if matrix[r][c] == "1":
                        dp[r][c] = 1 + min(dp[r][c-1],dp[r-1][c],dp[r-1][c-1])
                    else:               #匹配到最小的。如果是正方形的时三个方向都会是一样的值
                        dp[r][c] = 0
                maxsquare = max(maxsquare,dp[r][c])
        return maxsquare * maxsquare



    # 198. House Robber
    # Input: nums = [1,2,3,1]
    # Output: 4
    # Input: nums = [2,7,9,3,1]
    # Output: 12
    # https://leetcode.com/problems/house-robber/


    def rob(self, nums):
        # [rob1,rob2,n,n+1,...]
        rob1,rob2 = 0,0     # max can rob for the pervous two house
        for n in nums: # current house that we are at / do not rob
            temp = max(n+rob1,rob2) # 比较大小当前抢的大还是跳过大
            rob1 = rob2     #rob1 移动到下一个点
            rob2 = temp     #rob2 记录当前最大值
        return rob2

    # 213. House Robber II
    # Input: nums = [2,3,2]
    # Output: 3
    # Input: nums = [1,2,3,1]
    # Output: 4
    # https://leetcode.com/problems/house-robber-ii/



    def rob2(self,nums):
        return max(nums[0],self.rob(nums[1:]),self.rob(nums[:-1]))
            # 尾巴和头不能连接将问题分为两个subarray来看找最大的


    # 91. Decode Ways
    # Input: s = "12"
    # Output: 2
    # Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
    # Input: s = "226"
    # Output: 3
    # Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
    # Input: s = "06"
    # Output: 0
    # Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
    # https://leetcode.com/problems/decode-ways/

    def numDecodings(self, s):
        dp = {len(s):1}         #base case原始设定是1
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":     #如果第一个是0这个位置的组合是0
                dp[i] = 0
            else:
                dp[i]=dp[i+1]   #数自己本身就是个组合所以跟随前面的累加

            if (i+1 <len(s) and (s[i] == "1" or s[i]=="2" and s[i+1] in "0123456")):
                dp[i]+=dp[i+2]      #如果是两位数的情况 加上前两个index的情况
        return dp[0]










a= [-2,1,-3,4,-1,2,1,-5,4]
object = Solution()
print(object.maxSubArray(a))
print(object.climbStairs(3))
print(object.isSubsequence("abc","ahbgdc"))
print(object.uniquePaths(3,7))
print(object.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(object.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(object.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(object.numSquares(12))
print(object.wordBreak("leetcode",["leet","code"]))
print(object.minDistance("horse","ros"))
print(object.isInterleave("aabcc","dbbca","aadbbcbcac"))
print(object.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(object.numDecodings("226"))