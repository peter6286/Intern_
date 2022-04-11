class Solution:
    # 56 · Two Sum

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        numdict = {}
        for i, num in enumerate(numbers):
            rem = target - num
            if rem not in numdict:
                # 保存当前遍历的元素并保存index
                numdict[num] = i
            else:
                # 如果rem在当前的dict中直接返回
                return [numdict[rem], i]

    # 609 · Two Sum - Less than or equal to target
    def two_sum5(self, nums, target):
        nums.sort()
        # 先确定排序是正确的
        count = 0
        n = len(nums)
        # 因为是排好序的用two pointer 可以确定比target小的范围
        for i in range(n):
            left = i
            right = n
            curr = i
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] <= target:
                    left = mid
                    curr = mid
                else:
                    right = mid

            count += curr - i
            # 找两端的值可以省去不少步骤
        return count

    # 891 · Valid Palindrome II
    
    def valid_palindrome(self, s: str) -> bool:
        if s is None:
            return False
        left, right = self.find(s, 0, len(s) - 1)
        # 判断最后一个形成不了palindrome的index
        if left >= right:
        # 如果是左边大于右边了直接是palindrome
            return True
        # left + 1 ，right -1 达到产出一个的效果
        return self.ispalindrome(s, left + 1, right) or self.ispalindrome(s, left, right - 1)

    def ispalindrome(self, s, left, right):
        left, right = self.find(s, left, right)
        return left >= right

    def find(self, s, left, right):
        # 找left right 不相等的index
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right



    # 6 · Merge Two Sorted Arrays
    def merge_sorted_array(self, a: List[int], b: List[int]) -> List[int]:
        ans = [0] * (len(a) + len(b))
        i, j, k = 0, 0, 0
        # 将两个list合并在一块所以答案list的长度得是a和b加起来的长度
        while k < len(ans):
            #  当k还有没到达两个合并长度的时候
            if i < len(a) and (len(b) <= j or a[i] < b[j]):
                # A 写入的时候的条件。b的长度写完了或者a的大小小于b
                ans[k] = a[i]
                i += 1
                k += 1
            else:
                ans[k] = b[j]
                j += 1
                k += 1
        return ans

    # 5 · Kth Largest Element
    def kth_largest_element(self, k: int, nums: List[int]) -> int:
        if not nums:
            return 0
        # 先用quicksort排序然后倒数的第k个元素就是答案
        self.quicksort(nums, 0, len(nums) - 1)
        return nums[-k]

    def quicksort(self, nums, start, end):
        # quick sort 有piviot的存在
        if start >= end:
            return
        # 将pivot刚好设置为left，right中间的点
        piv = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            # 用while 循环找左右pointer不在对应位置的pointer
            while left <= right and nums[left] < piv:
                left += 1
            while left <= right and nums[right] > piv:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # 左右两边继续做quicksort
        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)


    # 148 · Sort Colors

    def sort_colors(self, nums: List[int]):
        # 用partion隔开就达到了题目的要求了
        self.partion(nums, 1)
        self.partion(nums, 2)

    def partion(self, nums, k):
        lastptr = -1
        # 要从-1开始前移动pointer
        for i in range(len(nums)):
            if nums[i] < k:
                # 如果小于target的就让当前的i和lastpter换位
                # 依次做达到partion
                lastptr += 1
                nums[i], nums[lastptr] = nums[lastptr], nums[i]
        return nums



    # 366 · Fibonacci
    def fibonacci(self, n: int) -> int:
        # base case 的情况
        fib = [0, 0, 1]
        for i in range(3, n + 1, 1):
            # 从3开始循环
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]



    # 457 · Classical Binary Search

    # 经典二分法
    # 必须得背
    def findPosition(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1


    # 458 · Last Position of Target

    # 要找最右边的target值
    def last_position(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                # 因为要找最右边所以先确定end
                end = mid
            else:
                start = mid
        # 因为要找最右边的所以if stament得从end开始
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1





    # 14 · First Position of Target


    def binary_search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                # # 因为要找最右边的所以if stament得从end开始
                right = mid
            else:
                left = mid

        # 因为要找最右边的所以if stament得从start开始
        if nums[left] == target:
            return left

        if nums[right] == target:
            return right
        return -1


