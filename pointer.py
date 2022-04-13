class Solution:

    # 经典必备quick sort
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

    # 经典必背mergesort

    def mergesort(self, nums):
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



    # 75. Sort Colors
    def sortColors(self, nums):
        def partition(nums,k):
            lastptr = -1
            for i in range(len(nums)):
                if nums[i] < k:
                    lastptr +=1
                    nums[lastptr],nums[i] = nums[i],nums[lastptr]
            return nums
        partition(nums,1)
        partition(nums,2)
        return nums

    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self,nums):
        if not nums:
            return -1
        writer = 0
        for i in range(1, len(nums)):
            if nums[writer] != nums[i]:
                writer += 1
                nums[writer] = nums[i]
        # 第一个单词肯定是写入的
        return writer + 1


    # 80. Remove Duplicates from Sorted Array II

    def removeDuplicates2(self, nums):
        if not nums:
            return -1
        reader,writer,count = 1,0,1
        while reader < len(nums):
            if nums[reader] == nums[writer]:
                if count < 2:
                    writer +=1
                    count +=1
                    nums[writer] = nums[reader]

            else:
                writer += 1
                count = 1
                nums[writer] = nums[reader]
            reader +=1

        return writer + 1



    # 88. Merge Sorted Array

    def merge(self,nums1,m,nums2,n):
        res = [0] * (m + n)
        i = j = k = 0
        while i < m and j < n :
            if nums1[i] < nums2[j]:
                res[k] = nums1[i]
                i += 1
            else:
                res[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            res[k] = nums1[i]
            i += 1
            k += 1
        while j < n:
            res[k] = nums2[j]
            j += 1
            k += 1

        return res


    # 283. Move Zeroes
    def moveZeroes(self,nums):
        if len(nums) <= 1:
            return nums
        index_zero,pointer = 0,0
        while pointer < len(nums):
            if nums[index_zero] == 0:
                if nums[pointer]!=0:
                    nums[index_zero],nums[pointer]= nums[pointer],nums[index_zero]
                    index_zero += 1
                else:
                    pointer +=1

            else:
                index_zero +=1
                pointer +=1
        return nums










object=Solution()
print(object.sortColors([2,0,2,1,1,0]))
print(object.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(object.removeDuplicates2([0,0,1,1,1,1,2,3,3]))
print(object.merge([1,2,3,0,0,0],3,[2,5,6],3))
print(object.moveZeroes([0,1,0,3,12]))