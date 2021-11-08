class Solution:
    # 704. Binary Search
    # Input: nums = [-1,0,3,5,9,12], target = 9   Output: 4
    # Input: nums = [-1,0,3,5,9,12], target = 2   Output: -1

    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    #35. Search Insert Position
    # Input: nums = [1,3,5,6], target = 5   Output: 2
    # Input: nums = [1,3,5,6], target = 2   Output: 1

    def searchInsert(self, nums, target):
        left=0
        right = len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left

    #278. First Bad Version
    #Input: n = 5, bad = 4     Output: 4
    #Input: n = 1, bad = 1    Output: 1
    ''''

    def firstBadVersion(self, n):
        left=0
        right=n
        while left<right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right=mid
            else:
                left=mid+1
        return left

    '''

object = Solution()
print(object.search([1,3,5,6],5))
print(object.searchInsert([1,3,5,6],5))