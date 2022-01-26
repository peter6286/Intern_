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
    # Input: nums = [3,4,5,1,2]
    # Output: 1
    # Explanation: The original array was [1,2,3,4,5] rotated 3 times.
    # Input: nums = [4,5,6,7,0,1,2]
    # Output: 0
    # Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
    # Input: nums = [11,13,15,17]
    # Output: 11
    # Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

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


    # 162. Find Peak Element
    # Input: nums = [1,2,3,1]
    # Output: 2
    # Explanation: 3 is a peak element and your function
    # should return the index number 2.
    # Input: nums = [1,2,1,3,5,6,4]
    # Output: 5
    # Explanation: Your function can return either index number 1
    # where the peak element is 2, or index number 5 where the peak element is 6.
    # https://leetcode.com/problems/find-peak-element/

    def findPeakElement(self, nums):
        left,right = 0 ,len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid]< nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 374. Guess Number Higher or Lower
    # Input: n = 10, pick = 6
    # Output: 6
    # Input: n = 1, pick = 1
    # Output: 1
    # Input: n = 2, pick = 1
    # Output: 1
    # https://leetcode.com/problems/guess-number-higher-or-lower/

    def guessNumber(self, n):
        left,right = 0,n
        while left <= right:
            mid = (left+right)//2
            res = guess(mid)
            if res < 0 :
                right = mid - 1
            elif res > 0 :
                left = mid + 1
            else:
                return mid







object = Solution()
print(object.search([2,5,6,0,0,1,2],0))
print(object.search2([1,0,1,1,1],0))
print(object.findMin([3,4,5,1,2]))
print(object.findPeakElement([1,2,3,1]))




