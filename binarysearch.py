class Solution:
    # 278. First Bad Version
    # Input: n = 5, bad = 4
    # Output: 4
    # Explanation:
    # call isBadVersion(3) -> false
    # call isBadVersion(5) -> true
    # call isBadVersion(4) -> true
    # Then 4 is the first bad version.
    # https://leetcode.com/problems/first-bad-version/


    def isbadversion(self,n):
        left = 0
        right = n
        while left <= right:
            mid = (left+right)//2
            if isbadversion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


    # 35. Search Insert Position
    # Input: nums = [1,3,5,6], target = 5
    # Output: 2
    # Input: nums = [1,3,5,6], target = 2
    # Output: 1
    # Input: nums = [1,3,5,6], target = 7
    # Output: 4
    # https://leetcode.com/problems/search-insert-position/

    def searchinsert(self,nums,target):
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid +1
            else:
                return mid
        return left


    # 33. Search in Rotated Sorted Array
    # Input: nums = [4,5,6,7,0,1,2], target = 0
    # Output: 4
    # Input: nums = [4,5,6,7,0,1,2], target = 3
    # Output: -1
    # https://leetcode.com/problems/search-in-rotated-sorted-array/

    def search(self,nums,target):
        left,right = 0 ,len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # 81. Search in Rotated Sorted Array II
    # Input: nums = [2,5,6,0,0,1,2], target = 0
    # Output: true
    # Input: nums = [2,5,6,0,0,1,2], target = 3
    # Output: false
    # https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

    def search2(self,nums,target):
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] == nums[mid] and mid != left:
                    left +=1
                    continue
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False



    # 153. Find Minimum in Rotated Sorted Array
    def findMin(self, nums):
        res = nums[0]
        left,right = 0,len(nums)-1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break
            mid = (left+right)//2
            res = min(res,nums[mid])
            if nums[left] <= nums[mid]: #继续往右边搜最小的
                left = mid + 1
            else:
                right = mid - 1     #往左边搜最小的
        return res





object = Solution()
print(object.search([2,5,6,0,0,1,2],0))
print(object.search2([1,0,1,1,1],0))
print(object.findMin([3,4,5,1,2]))




