class Solution:

    # 78. Subsets

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


    def subsetsWithDup(self, nums):
        def backtrack(i,Curnum):
            ans.append(Curnum[:])
            for j in range(i,n):
                if j > i and nums[j]==nums[j-1]:
                    continue
                Curnum.append(nums[j])
                backtrack(j+1,Curnum)
                Curnum.pop()
        n=len(nums)
        nums.sort()
        ans=[]
        backtrack(0,[])
        return ans

object=Solution()
print(object.subsets([1,2,3]))
print(object.subsetsWithDup([1,2,2]))
