class Solution:

    # 经典二分 必背
    # 704. Binary Search
    def binarysearch(self, nums, target):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

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
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
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
            if nums[left] <= nums[mid]:     #正常的在在左半边找
                if nums[left] == nums[mid] and mid != left: # 检查mid和left的元素是一样的
                    left +=1        # 如果是一样的就往前
                    continue
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:    # left是rotate后最大的所以回到右半边找
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
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid
        return min(nums[start], nums[end])




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
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]: #刚好是中间大的元素返回
                return mid
            if nums[mid]< nums[mid+1]:  #右边比较大移动到右边的点上再比较
                left = mid + 1
            else:
                right = mid - 1     #左边的点比较大移动到左边上的点后再比较
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

    # 34. Find First and Last Position of Element in Sorted Array
    # Input: nums = [5,7,7,8,8,10], target = 8
    # Output: [3,4]
    # Input: nums = [5,7,7,8,8,10], target = 6
    # Output: [-1,-1]
    # Input: nums = [], target = 0
    # Output: [-1,-1]
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

    def searchRange(self, nums, target):
        left,right = 0,len(nums)-1
        while left < right:
            if nums[left]!= target:
                left += 1
            elif nums[right]!=target:
                right-=1
            elif nums[left]== target and nums[right]==target:
                return [left,right]
        return [-1,-1]


    # 349. Intersection of Two Arrays
    # Input: nums1 = [1,2,2,1], nums2 = [2,2]
    # Output: [2]
    # Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    # Output: [9,4]
    # Explanation: [4,9] is also accepted.
    # https://leetcode.com/problems/intersection-of-two-arrays/

    def intersection(self, nums1, nums2):
        d = { }
        res = []
        for n in nums1:
            d[n]=1

        for n in nums2:
            #  # Check if n is in dictionary and not in the result
            if n in d and d[n]:
                res.append(n)
                d[n] -= 1
            # It will set the value of d[n] = 0 which will indicate we already added n in result
        return res


    # 350. Intersection of Two Arrays II
    # Input: nums1 = [1,2,2,1], nums2 = [2,2]
    # Output: [2,2]
    # Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    # Output: [4,9]
    # Explanation: [9,4] is also accepted.
    # https://leetcode.com/problems/intersection-of-two-arrays-ii/

    def intersection2(self, nums1, nums2):
        d = {}
        res = []
        for n in nums1:     #dict 累加
            if n not in d:
                d[n]=1
            else:
                d[n] += 1

        for n in nums2:
            if n in d and d[n] > 0 :
                res.append(n)       #继续输入进去直到dict值没有为止
                d[n] -= 1
        return res


    # 300. Longest Increasing Subsequence
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    # Input: nums = [0,1,0,3,2,3]
    # Output: 4
    # Input: nums = [7,7,7,7,7,7,7]
    # Output: 1
    # https://leetcode.com/problems/longest-increasing-subsequence/

    # [1,2,4,3]
    # LIS[3] = 1 , LIS[2] = max(1,1+LIS[3]),LIS[1] = max(1,1+LIS[2]),1+LIS[3]),LIS[0]=max(LIS[i],1+LIS[j])
    def lengthOfLIS(self, nums):
        LIS = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)

    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - 1

        # Find index of x or the closest val to x
        val, idx = arr[0], 0
        while l <= r:
            m = (l + r) // 2
            curDiff, resDiff = abs(arr[m] - x), abs(val - x)
            # 找离x最近的值
            if (curDiff < resDiff or (curDiff == resDiff and arr[m] < val)):
                #重新设置inde和val的值
                val, idx = arr[m], m
            # 然后再确认搜索的范围
            if arr[m] < x:
                l = m + 1
            elif arr[m] > x:
                r = m - 1
            else:
                break

        l = r = idx
        for i in range(k - 1):
            if l == 0:
                r += 1
            elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
                l -= 1
            else:
                r += 1
        return arr[l:r + 1]















object = Solution()
print(object.search([2,5,6,0,0,1,2],0))
print(object.search2([1,0,1,1,1],0))
print(object.findMin([3,1,2]))
print(object.findPeakElement([1,2,3,1]))
print(object.searchRange([],0))
print(object.intersection([4,9,5],[9,4,9,8,4]))
print(object.intersection2([1,2,2,1],[2,2]))
print(object.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(object.findClosestElements([1,2,3,4,5],4,-1))



