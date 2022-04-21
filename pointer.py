class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        def partition(nums, k):
            lastptr = -1
            for i in range(len(nums)):
                if nums[i] < k:
                    lastptr += 1
                    nums[lastptr], nums[i] = nums[i], nums[lastptr]
            return nums

        partition(nums, 1)
        partition(nums, 2)
        return nums

    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums):
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
        reader, writer, count = 1, 0, 1
        while reader < len(nums):
            if nums[reader] == nums[writer]:
                if count < 2:
                    writer += 1
                    count += 1
                    nums[writer] = nums[reader]

            else:
                writer += 1
                count = 1
                nums[writer] = nums[reader]
            reader += 1

        return writer + 1

    # 88. Merge Sorted Array

    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1

    # 283. Move Zeroes
    def moveZeroes(self, nums):
        if len(nums) <= 1:
            return nums
        index_zero, pointer = 0, 0
        while pointer < len(nums):
            if nums[index_zero] == 0:
                # 确认当前的index_zero指针上有0找可以替换的点
                # 移动pointer找替换点
                if nums[pointer] != 0:
                    # 当pointer不是0的时候替换并将index_zero指针指向下一位
                    nums[index_zero], nums[pointer] = nums[pointer], nums[index_zero]
                    index_zero += 1
                else:
                    # 当前的指针不能做替换所以pointer往前跳一位
                    pointer += 1
            else:
                # 如果当前index不等于0的时候指针都往前跳一位
                index_zero += 1
                pointer += 1
        return nums

    # 215. Kth Largest Element in an Array
    def findKthLargest(self, nums, k):
        if not nums:
            return -1
        self.quicksort(nums, 0, len(nums) - 1)
        return nums[-k]

    # 347. Top K Frequent Elements

    def topKFrequent(self, nums, k):
        if len(nums) <= 1:
            return nums
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res

    # 349. Intersection of Two Arrays
    def intersection(self, nums1, nums2):
        d = {}
        res = []
        for n in nums1:
            d[n] = 1

        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                # 去重
                d[n] -= 1
        return res

    # 350. Intersection of Two Arrays II
    def intersect(self, nums1, nums2):
        d = {}
        res = []
        for n in nums1:
            d[n] = 1 + d.get(n, 0)
        for n in nums2:
            if n in d and d[n]:
                res.append(n)
                # 去重
                d[n] -= 1
        return res

    # 845. Longest Mountain in Array
    def longestMountain(self, arr):
        longestHeight = 0

        # 忽略第一个和最后一个元素因为他不会是peak元素
        currIdx = 1
        while currIdx < len(arr) - 1:
            # 寻找peak的元素
            isPeak = arr[currIdx] > arr[currIdx - 1] and arr[currIdx] > arr[currIdx + 1]
            if not isPeak:
                # if not peak then continue
                currIdx += 1
                continue
            # if we found peak - now time to expand to left and right to measure height
            # start with second adjacent from left and right
            # 找到符合peak的index 往左右两边拓展
            # 检查的时候已经确认index 所以从第二个开始
            leftIdx = currIdx - 2
            rightIdx = currIdx + 2
            # 检查是否在范围之内
            while leftIdx >= 0 and arr[leftIdx] < arr[leftIdx + 1]:
                leftIdx -= 1

            while rightIdx < len(arr) and arr[rightIdx] < arr[rightIdx - 1]:
                rightIdx += 1
            # 计算当前的大小然后比较选出最大的
            currHeight = rightIdx - leftIdx - 1
            longestHeight = max(longestHeight, currHeight)

            # 因为已经检查过前后的两位pointer所以直接将current移动
            currIdx = rightIdx
        return longestHeight

    def findpeak(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:  # 刚好是中间大的元素返回
                return mid
            if nums[mid] < nums[mid + 1]:  # 右边比较大移动到右边的点上再比较
                left = mid + 1
            else:
                right = mid - 1  # 左边的点比较大移动到左边上的点后再比较
        return left

    def multiply(self, num1, num2):
        num1, num2 = int(num1), int(num2)
        return str(num1 * num2)

    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next

    # 86. Partition List
    def partition(self, head, x):
        dummy_l, dummy_r = ListNode(), ListNode()
        left, right = dummy_l, dummy_r
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.tail = dummy_r.next
        right.tail = None
        return dummy_l.next

    # 141. Linked List Cycle
    def hasCycle(self, head):
        numset = set()
        while head:
            if head not in numset:
                numset.add(head)
            else:
                return True
            head = head.next
        return False



    # 160. Intersection of Two Linked Lists
    def getIntersectionNode(self,headA,headB):
        nodeset = set()
        while headA:
            nodeset.add(headA)
            headA = headA.next
        while headB:
            if headB not in nodeset:
                headB = headB.next
            else:
                return headB
        return None



    # 234. Palindrome Linked List
    def isPalindrome(self,head):
        num = []
        while head:
            num.append((head.val))
            head = head.next
        return num == num[::-1]



object = Solution()
print(object.sortColors([2, 0, 2, 1, 1, 0]))
print(object.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(object.removeDuplicates2([0, 0, 1, 1, 1, 1, 2, 3, 3]))
print(object.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(object.moveZeroes([0, 1, 0, 3, 12]))
print(object.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(object.findpeak([2, 1, 4, 7, 3, 2, 5]))
print(object.longestMountain([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(object.multiply("2", "3"))
