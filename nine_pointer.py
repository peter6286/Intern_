class Solution:

    # 125. Valid Palindrome

    def ispalindrome(self,s):
        left,right = 0,len(s)-1
        while left < right:
            while left < right and not self.is_valid(s[left]):
                left +=1
            while left < right and not self.is_valid(s[right]):
                right -=1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True

    def is_valid(self,s):
        return s.isalnum()


    # 680. Valid Palindrome II


    def validPalindrome(self, s):
        if s is None:
            return False
        left,right = self.finddifference(0,len(s)-1) #找到形成不了palindrome的左右下标
        if left >= right:           # 先检查原本是否已经是palindrome
            return True
        return isPalindrome(s,left+1,right) or isPalindrome(s,left,right-1)
            #如果还不是移动一位再检查
    def isPalindrome(self,left,right):
        left,right = self.finddifference(s,left,right)
        return left>=right          #如果左边大于右边代表通过了

    def finddifference(self,s,left,right):  #检查并找到形成不了palindrome的地方
        while left < right:
            if s[left] != s[right]:
                return left,right
            left +=1
            right -=1
        return left,right



    # 1. Two Sum
    def twosum(self,nums,target):
        numdict = {}
        for i ,num in enumerate(nums):
            remainder = target - num
            if remainder not in numdict:
                numdict[num] = i
            else:
                return [numdict[remainder],i]

    # 167. Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1


    #  15. 3Sum
    def threeSum(self, nums):
        res = []
        nums.sort()
        if not nums or len(nums)<3:
            return res

        for i,target in enumerate(nums):
            if i>0 and target == nums[i-1]:  #过滤掉重复的target
                continue
                                                #选一个其他两个做two sum
            l,r = i+1,len(nums)-1
            while l < r:                    #经典two pointer 算法
                threesum = target + nums[l] + nums[r]
                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([target,nums[l],nums[r]])    #将当前结果加入然后继续往后遍历
                    l+=1
                    while nums[l] == nums[l-1] and l <r:        #如果是一样的就继续跳过
                        l+=1
        return res


    # 611. Valid Triangle Number

    def triangleNumber(self, nums):
        res = 0
        if not nums and len(nums)<3:
            return res
        nums.sort()
        for i in range(2,len(nums)):
            target = nums[i]
            left,right = 0,i-1
            while left < right:
                twosum = nums[left]+nums[right]
                if twosum > target:
                    res += right - left
                    right -=1
                else:
                    left +=1
        return res


    # 454. 4Sum II
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        numdict = {}
        for a in nums1:
            for b in nums2:
                sum = a + b
                numdict[sum]=numdict.get(sum,0)+1
        count = 0
        for c in nums3:
            for d in nums4:
                sum = c + d
                count += numdict.get(-sum,0)
        return count


    # 18. 4Sum
    def fourSum(self, nums, target):
        nums.sort()
        res,quad = [],[]
        def ksum(k,start,target):
            if k!=2:      # 等于2的时候是base case用two sum的方法两个pointer
                for i in range(start,len(nums)-k+1):    #len(nums)-k+1为后面做好空格
                    if i>start and nums[i] == nums[i-1]:    #将重复的去掉
                        continue
                    quad.append(nums[i])
                    ksum(k-1,i+1,target-nums[i])   #减去当前点的然后再用two sum做
                    quad.pop()
                return


            left,right = start,len(nums)-1
            while left < right:
                twosum = nums[left]+nums[right]
                if twosum < target:
                    left +=1
                elif twosum > target:
                    right-=1
                else:
                    res.append(quad+[nums[left],nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
        ksum(4,0,target)
        return res

    # partition array 经典分区
    def partitionarray(self,nums,k):
        if not nums:
            return 0
        left,right = 0,len(nums)-1
        while left <= right:  #如果用left<right 循环在left==right结束，还需一个判断nums[left]
            # 左指针寻找比k大的数
            while left <= right and nums[left]<k:
                left +=1
            # 右执政寻找比k小的数
            while left <= right and nums[right]>=k:
                right-=1
            if left <= right :
                #交换左右指针两个指针上的数都到了正确的index上
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        return left



    # 144 · Interleaving Positive and Negative Numbers
    #与wiggle sort不一样这里知道pivot是多少
    #负多正少，left=1，right=length-1
    #负少正多，left=0，right=length-2
    #正负相等，left=0，right=length-1

    def rearange(self,A):
        neg_cnt = self.partiton(A)
        pos_cnt = len(A)-neg_cnt
        left = 1 if pos_cnt < neg_cnt else 0
        right = len(A) - (2 if pos_cnt > neg_cnt else 1)
        while left < right:
            A[left],A[right]=A[right],A[left]
            left+=2
            right-=2
        return A


    def partiton(self,nums):
        left,right = 0,len(nums)-1
        while left <= right:
            while left<=right and nums[left]<0:
                left +=1
            while left<= right and nums[right]>=0:
                right -=1
            if left<=right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        return left

    # 324. Wiggle Sort II
    def wiggleSort(self, nums):
        nums.sort()
        print(nums)
        half = len(nums[::2])       #nums[1::2] 奇数位的index
        print(nums[::2])            #nums[::2] 偶数位的index
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]  #nums里的偶数index放排序后中间较小的index
        return nums


    # 75. Sort Colors
    def sortColors(self, nums):
        # 因为sort中颜色用数字代表所以partion两次数字即可
        self.partitioncolor(nums,1)
        self.partitioncolor(nums,2)
        return nums

    def partitioncolor(self,nums,k):
        # 指向<k区间的最后一个元素
        last_smallp= -1
        for i in range(len(nums)):
            # 如果nums[i]<k，需要交换并右移指针
            if nums[i]<k:
                #指针先右移一位，指向当前元素对应位置
                #然后进行交换
                last_smallp +=1
                nums[last_smallp],nums[i]=nums[i],nums[last_smallp]
        return last_smallp +1



    # 143 · Sort Colors II
    def sortColors2(self, colors, k):
        if not colors or len(colors)<2:
            return
        self.sort(colors,1,k,0,len(colors)-1)
        return colors

    def sort(self,colors,color_from,color_to,index_from,index_to):
        if color_from == color_to:
            return

        mid_color = (color_from+color_to)//2
        left,right = index_from,index_to
        while left <= right:
            while left <= right and colors[left]<mid_color:
                left +=1
            while left <= right and colors[right]>=mid_color:
                right-=1
            if left <= right:
                colors[left],colors[right]=colors[right],colors[left]
                left+=1
                right-=1

        self.sort(colors,color_from,mid_color,index_from,right)
        self.sort(colors,mid_color+1,color_to,left,index_to)




    # 283. Move Zeroes
    def moveZeroes(self, nums):
        fillpointer,movepointer = 0,0
        while movepointer < len(nums):
            if nums[movepointer] != 0:
                if fillpointer != movepointer:
                    nums[fillpointer],nums[movepointer]=nums[movepointer],nums[fillpointer]
                fillpointer +=1
            movepointer +=1
        return nums

    def moveZeroes2(self, nums):
        l, r = 0, 0
        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1
            else:
                l += 1
                r += 1











object = Solution()
print(object.ispalindrome("A man, a plan, a canal: Panama"))
print(object.twosum([2,7,11,15],9))
print(object.threeSum([-1,0,1,2,-1,-4]))
print(object.triangleNumber([2,2,3,4]))
print(object.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
print(object.fourSum([1,0,-1,0,-2,2],0))
print(object.rearange([-1, -2, -3, 4, 5, 6]))
print(object.wiggleSort([-1, -2, -3, 4, 5, 6]))
print(object.sortColors([2,0,2,1,1,0]))
print(object.sortColors2([3,2,2,1,4],4))
print(object.moveZeroes([0,1,0,3,12]))