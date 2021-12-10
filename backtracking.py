class Solution:
    def subsets(self, nums):
        ret = []
        def dfs (nums, path, ret):
            ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]], ret)
        dfs(nums, [], ret)
        return ret



object=Solution()
print(object.subsets([1,2,3]))
