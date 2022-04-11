class Solution:

    # 经典二分 必背
    # 704. Binary Search
    def binarysearch(self,nums,target):
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


    # quick sort
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, start, end):
        if start >= end:
            return
        left, right = start, end
        piv = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < piv:
                left += 1
            while left <= right and nums[right] > piv:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)



    def mergesort(self, nums: List[int]) -> List[int]:
        #  base case 检查的是否长度为1
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        self.mergesort(left)
        self.mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums

