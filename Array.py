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
                    writer += 1     #确定可以写入后再往前
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

    #Gas station 134
    #Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    # Output: 3
    # Input: gas = [2,3,4], cost = [3,4,3]
    # Output: -1
    def gas(self, gas, cost):
        if (sum(cost)-sum(gas)<0):
            return -1
        gas_tank = 0  # gas available in car till now
        start_index = 0  # Consider first gas station as starting point

        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            if gas_tank < 0:  # the car has deficit of petrol
                start_index = i + 1  # change the starting point
                gas_tank = 0  # make the current gas to 0, as we will be starting again from next station

        return start_index


    ###不会
    def hIndex(self, citations):
        if len(citations) == 0:
            return 0

        res = 0
        citations.sort(reverse = True)

        if citations[-1] >= len(citations):
            return len(citations)

        for i in range(1, len(citations)+1):
            if i > citations[i-1]:
                res = i-1
                break
        return res

    def containduplicate(self,nums):
        hashNum = {} #hash table
        for i in nums:
             if i not in hashNum:
                hashNum[i] = 1
             else:
                return True
        return False


    def canJump(self, nums):
        reachableIndex = 0
        if len(nums)==1:
            return True
        for curr in range(len(nums)):
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr] #更新最新的reachable
            if curr == reachableIndex:  #如果没有变化给他掐断/到了最尾巴
                break
        return reachableIndex >=len(nums)-1


    def jump(self, nums):
        if len(nums)==1:
            return 0

        reachableIndex = 0
        bestReachableIndex = 0
        jump = 0

        for curr in range(len(nums)):
            temp= nums[curr]
            if curr + nums[curr] >= reachableIndex:
                reachableIndex = curr + nums[curr]

            if curr == bestReachableIndex:          #到位置后要么step加一
                jump += 1
                bestReachableIndex = reachableIndex
                if bestReachableIndex >= len(nums) - 1:
                    return jump

    def maxProfit(self, prices):
        if not prices:
            return 0

        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit





object = Solution()
print(object.removeElement([0,1,2,2,3,0,4,2], 2))
print(object.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(object.removeDuplicates2([0,0,1,1,1,1,2,3,3]))
print(object.rotate([1,2,3,4,5,6,7],3))
print(object.getHint("1123","0111"))
print(object.gas([1,2,3,4,5],[3,4,5,1,2]))
print(object.hIndex([3,0,6,1,5]))
print(object.hIndex([7,8,9]))
print(object.containduplicate([1,2,3,1]))
print(object.canJump([2,3,1,1,4]))
print(object.canJump([3,2,1,0,4]))
print(object.jump([2,1,1,3,4]))
print(object.jump([2,3,0,1,4]))
print(object.maxProfit([7,1,5,3,6,4]))
