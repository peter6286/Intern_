class Solution:
    #27
    def removeElement(self, nums, val):
        len_ = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[len_] = nums[i]
                len_ += 1
        return len_
    #26
    def removeDuplicates(self,nums):
        len_ = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # 因为已经sorted好跟前一个比较就行
                nums[len_] = nums[i]
                len_ += 1
        return nums
    #80
    def removeDuplicates2(self, nums) :
        reader, writer, count = 1, 0, 1 #reader从第二个开始读/

        while reader < len(nums):

            if nums[reader] == nums[writer]: #如果一样
                if count < 2:       #检查是否出现两次
                    writer += 1
                    nums[writer] = nums[reader]
                    count += 1
            else:       #如果不一样重置count变1
                writer += 1
                nums[writer] = nums[reader]
                count = 1
            reader += 1
        return writer+1

    #189
    def rotate(self, nums, k):
        for c in range(k):
            previous = nums[-1] #initiate a first previous
            for i in range(len(nums)):
                temp = nums[i] #hodl nums[i]
                nums[i] = previous #overwrite the current index
                previous = temp #swap the value
        return nums

    #299
    def getHint(self, secret, guess):

        # The main idea is to understand that cow cases contain the bull cases

        # This loop will take care of "bull" cases
        bull=0
        for i in range(len(secret)):
            bull += int(secret[i] == guess[i])

        # This loop will take care of "cow" cases
        cows=0
        for c in set(secret):
            a=secret.count(c)
            b=guess.count(c)
            cows += min(a, b)

        return f"{bull}A{cows-bull}B"







object = Solution()
print(object.removeElement([0,1,2,2,3,0,4,2], 2))
print(object.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(object.removeDuplicates2([0,0,1,1,1,1,2,3,3]))
print(object.rotate([1,2,3,4,5,6,7],3))
print(object.getHint("1123","0111"))