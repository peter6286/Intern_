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








object = Solution()
print(object.ispalindrome("A man, a plan, a canal: Panama"))
print(object.twosum([2,7,11,15],9))
print(object.threeSum([-1,0,1,2,-1,-4]))
print(object.triangleNumber([2,2,3,4]))
print(object.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
print(object.fourSum([1,0,-1,0,-2,2],0))