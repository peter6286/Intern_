class Solution:

    # 78.
    # Input: nums = [1,2,3]
    # Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    # Input: nums = [0]
    # Output: [[],[0]]

    def subsets(self, nums):
        res = []
        subset=[]
        def dfs(i):
            if i >= len(nums):
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
                if j > i and nums[j]==nums[j-1]:  #如果和前一个是一样的
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
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])       #repeated the current index
            dfs(i,cur,total+candidates[i])
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
                if candidates[i] == perv:
                    continue
                cur.append(candidates[i])
                backtrack(cur,i+1,target-candidates[i])
                cur.pop()
                perv = candidates[i]
        backtrack([],0,target)
        return res



object=Solution()
print(object.subsets([1,2,3]))
print(object.subsetsWithDup([1,2,2]))
print(object.combinationSum([2,3,6,7],7))
print(object.combinationSum2([10,1,2,7,6,1,5],8))
