class Solution:

    # 78.
    # Input: nums = [1,2,3]
    # Output: [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
    # Input: nums = [0]
    # Output: [[],[0]]

    def subsets(self, nums):
        res = []
        subset=[]
        def dfs(i):
            if i >= len(nums):  #base case nums全遍历过后输出
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

    # 90. Subsets II
    # Input: nums = [1,2,2]
    # Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
    # Input: nums = [0]
    # Output: [[],[0]]

    def subsetsWithDup(self, nums):
        def backtrack(i,Curnum):
            ans.append(Curnum[:])
            for j in range(i,n):
                if j > i and nums[j]==nums[j-1]:  #确定j要比i大，如果和前一个是一样的
                    continue
                Curnum.append(nums[j])
                backtrack(j+1,Curnum)
                Curnum.pop()
        n=len(nums)
        nums.sort()
        ans=[]
        backtrack(0,[])
        return ans


    # 39. Combination Sum
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    #  Input: candidates = [2,3,5], target = 8
    # Output: [[2,2,2,2],[2,3,3],[3,5]]
    # Input: candidates = [2], target = 1
    # Output: []

    def combinationSum(self, candidates, target):
        res = []
        def dfs(i,cur,total):
            if total == target:             #如果到了一样的
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:      #超过了target
                return

            cur.append(candidates[i])       #repeated the current index
            dfs(i,cur,total+candidates[i])  # include 的current index
            cur.pop()
            dfs(i+1,cur,total)      # i 移动到下一个index所以会exclude目前index

        dfs(0,[],0)
        return res

    # 40. Combination Sum II
    # Input: candidates = [10,1,2,7,6,1,5], target = 8
    # Output:  [[1,1,6],[1,2,5],[1,7],[2,6]]
    # Input: candidates = [2,5,2,1,2], target = 5
    # Output: [[1,2,2],[5]]

    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def backtrack(cur,pos,target):  # cur 目前的组合，pos 目前过的位置，target会随着逐渐减少到0
            if target == 0 :
                res.append(cur[:])
            if target <= 0 :
                return
            perv = -1
            for i in range (pos,len(candidates)):
                if candidates[i] == perv:       # 跳过之前的node candidate only use by once
                    continue
                cur.append(candidates[i])
                backtrack(cur,i+1,target-candidates[i])
                cur.pop()
                perv = candidates[i]
        backtrack([],0,target)
        return res

    # 216. Combination Sum III
    # Input: k = 3, n = 7
    # Output: [[1,2,4]]
    # Input: k = 3, n = 9
    # Output: [[1,2,6],[1,3,5],[2,3,4]]

    def combinationSum3(self, k, n):
        res = []

        def backtrack(num, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack[:])
                    return
            for x in range(num + 1, 10):        # 1-10 的数相加 #
                if x <= target:     # target 会随之减小往后越大的数也会跳过
                    stack.append(x)
                    backtrack(x, stack, target - x)      #减去目前的大小达到base case
                    stack.pop()
        backtrack(0, [], n)
        return res

    # 377. Combination Sum IV
    # Given an array of distinct integers nums and a target integer
    # target, return the number of possible combinations that add up to target.
    # Input: nums = [1,2,3], target = 4
    # Output: 7
    # Explanation:
    # The possible combination ways are:
    # (1, 1, 1, 1)
    # (1, 1, 2)
    # (1, 2, 1)
    # (1, 3)
    # (2, 1, 1)
    # (2, 2)
    # (3, 1)
    # Note that different sequences are counted as different combinations.
    # [1,1,2,4,7]
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)     # [0,0,0,0,0] ----> [1,1,2,4,7]
        dp[0] = 1
        for i in range(1, target + 1):  # 从1一直到target填充
            for j in nums:      #遍历nums中的每一个元素
                if i - j >= 0:  #遍历nums的每一个元素检查减去后是否等于大于1判断有多少种解法
                    dp[i] += dp[i - j]  #填充进去
        return dp[target]


    # 46. Permutations
    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    # Input: nums = [0,1]
    # Output: [[0,1],[1,0]]


    def permute(self, nums):
        res = []
        def backtreack( nums, cur, res):
            if len(nums) == 0:      #当没有nums的时候
                res.append(cur[:])
                return

            for i in range(len(nums)):
                cur.append(nums[i])
                backtreack(nums[:i] + nums[i + 1:], cur , res) #在当前遍历的item除外的都可以在nums里 choose one 选别的
                cur.pop()
        backtreack(nums, [], res)           #确保nums在位置上
        return res

    # 47. Permutations II
    # Input: nums = [1,1,2]
    # Output:
    # [[1,1,2],
    #  [1,2,1],
    #  [2,1,1]]
    # Input: nums = [1,2,3]
    # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    def permuteUnique(self, nums):
        res = []
        count = { n:0 for n in nums}
        for n in nums :
            count[n]+=1
        def dfs(stack):
            if len(stack) == len(nums):      #base case perm的长度
                res.append(stack[:])
                return
            for n in count:
                if count[n] > 0:  #只有比count大才能进入perm，小于代表用完了
                    stack.append(n)
                    count[n]-=1
                    dfs(stack)     #backtracking
                    count[n]+=1
                    stack.pop()
        dfs([])
        return res

    #31. Next Permutation
    # Input: nums = [1,2,3]
    # Output: [1,3,2]
    # Input: nums = [3,2,1]
    # Output: [1,2,3]
    # Input: nums = [1,1,5]
    # Output: [1,5,1]


    def nextPermutation(self, nums):
        n = len(nums)
        pivot = 0
        for i in range (n-1,0,-1):   #从后开始确定pivot的位置，从后升序打断的点是pivot
            if nums[i-1] < nums[i]:
                pivot = i
                break
        if pivot == 0 :     #edge case 如果pivot是0直接sort
            nums.sort()
            return nums
        swap = n-1
        while nums[pivot-1] >= nums[swap]:      #循环到比pivot刚好比pivot大的点上，因为是升序所以找到的肯定是比他大一点的
            swap -=1
        nums[pivot-1],nums[swap] = nums[swap],nums[pivot-1]     #找到位置后进行swap
        nums[pivot:] = sorted(nums[pivot:])     #将剩余的反转排序
        return nums


    # 17. Letter Combinations of a Phone Number
    # Input: digits = "23"
    # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    # Input: digits = ""
    # Output: []
    # Input: digits = "2"
    # Output: ["a","b","c"]


    def letterCombinations(self, digits):
        res = []
        digittoChar = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        def backtrack(i,currstr):  # i每个digit的index所以从0开始 currstr是目前i里面的character
            if len(currstr)==len(digits):   #base case 如果currstr的长度等于digit的长度
                res.append(currstr)
                return
            for c in digittoChar[digits[i]]:    #循环每个digit里的character组合成string
                backtrack(i+1,currstr+c)

        if digits:
            backtrack(0,"")
        return res


    # 93. Restore IP Addresses
    # Input: s = "25525511135"
    # Output: ["255.255.11.135","255.255.111.35"]
    # Input: s = "0000"
    # Output: ["0.0.0.0"]
    # Input: s = "101023"
    # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

    def restoreIpAddresses(self, s):
        res =[]
        if len(s) > 12 :   #如果多于12位直接无效
            return res
        def backtrack(i,dots,curip):
            if dots == 4 and i == len(s):      #base case 1 刚好有4个dots长度刚好是s
                res.append(curip[:-1])          #压入输出去掉最后一个点
                return
            if dots > 4:                    # base case 2 超过了4个dots
                return

            for j in range (i,min(i+3,len(s))):  #从j点起跑三个index
                if int(s[i:j+1])<256 and (i==j or s[i]!= "0"):  #检查这三个数是不是小于255 同时第一位不能是0或者单独是0
                    backtrack(j+1,dots+1,curip+s[i:j+1]+".")
        backtrack(0,0,"")
        return res

    # 216. Combination Sum III
    # Input: k = 3, n = 7
    # Output: [[1,2,4]]
    # Input: k = 3, n = 9
    # Output: [[1,2,6],[1,3,5],[2,3,4]]

    def combinationSum3(self, k, n):
        res = []
        def backtrack(num,stack,target):
            if len(stack)==k:
                if target ==0 :
                    res.append(stack)
                return

            for x in range (num+1,10):
                if x <= target:
                    backtrack(x,stack+[x],target-x)

        backtrack(0,[],n)
        return res













object=Solution()
print(object.subsets([1,2,3]))
print(object.subsetsWithDup([1,2,2]))
print(object.combinationSum([2,3,6,7],7))
print(object.combinationSum2([10,1,2,7,6,1,5],8))
print(object.combinationSum3(3,9))
print(object.combinationSum4([1,2,3],4))
print(object.permute([1,2,3]))
print(object.permuteUnique([1,1,2]))
print(object.nextPermutation([1,2,3]))
print(object.letterCombinations("23"))
print(object.restoreIpAddresses("25525511135"))

