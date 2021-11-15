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

    #217. Contains Duplicate
    # Input: nums = [1,2,3,1]   Output: true
    # Input: nums = [1,1,1,3,3,4,3,2,4,2]   Output: true
    def containduplicate(self,nums):
        hashNum = {} #hash table
        for i in nums:
             if i not in hashNum:
                hashNum[i] = 1
             else:
                return True
        return False

    # 55. Jump Game
    # Input: nums = [2,3,1,1,4]    Output: true
    # Input: nums = [3,2,1,0,4]    Output: false

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

    #不会
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

    #Best Time to Buy and Sell Stock 121
    # Input: prices = [7,1,5,3,6,4]    Output: 5
    #Input: prices = [7, 6, 4, 3, 1]   Output: 0

    def maxProfit1(self, prices):
        if not prices:
            return 0
        maxProfit = 0
        minPurchase = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit

    # Best Time to Buy and Sell Stock II 122.
    #Input: prices = [7,1,5,3,6,4]   Output: 7
    # Input: prices = [1,2,3,4,5]  Output: 4
    def maxProfit2(self, prices):
        if len(prices) == 1: # edge case
            return 0

        # take down positive daily return only
        profit = []
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1]))
        return sum(profit)



    '''  不会
    # 188. Best Time to Buy and Sell Stock IV
    # Input: k = 2, prices = [2,4,1]   Output: 2
    # Input: k = 2, prices = [3,2,6,5,0,3] Output: 7
    
    def maxProfit3(self, prices):
        if not prices:
            return 0
    # forward traversal, profits record the max profit
    # by the ith day, this is the first transaction
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)
    # backward traversal, max_profit records the max profit
    # after the ith day, this is the second transaction
        total_max = 0
        max_profit = 0
        current_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            current_max = max(current_max, prices[i])
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])

        return total_max
    '''

    # 11. Container With Most Water
    # Input: height = [1,1]  Output: 1
    # Input: height = [4,3,2,1,4]  Output: 16


    def maxArea(self, height):

        # length of input array
        size = len(height)

        # two pointers, left init as 0, right init as size-1
        left, right = 0, size-1

        # maximal width between leftmost stick and rightmost stick
        max_width = size - 1

        # area also known as the amount of water
        area = 0

        # trade-off between width and height
        # scan each possible width and compute maximal area
        for width in range(max_width, 0, -1):

            if height[left] < height[right]:
                # the height of lefthand side is shorter
                area = max(area, width * height[left])

                # update left index to righthand side
                left += 1

            else:
                # the height of righthand side is shorter
                area = max(area, width * height[right])

                # update right index to lefthand side
                right -= 1

        return area


    # 334. Increasing Triplet Subsequence
    # Input: nums = [1,2,3,4,5]   Output: true
    # Input: nums = [5,4,3,2,1]   Output: false
    # Input: nums = [2,1,5,0,4,6]   Output: true

    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


    #128. Longest Consecutive Sequence
    # Input: nums = [100,4,200,1,3,2]   Output: 4
    # Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9
    def longestConsecutive(self, nums):
        nums.sort()
        longest, cur_longest = 0, min(1, len(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] :
                continue
            if nums[i] == nums[i - 1] + 1:
                cur_longest += 1
            else:
                longest, cur_longest = max(longest, cur_longest), 1
        return max(longest, cur_longest)

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
#print(object.maxProfit([7,1,5,3,6,4]))
#print(object.maxProfit3([3,3,5,0,0,3,1,4]))
print(object.maxArea([1,8,6,2,5,4,8,3,7]))
print(object.increasingTriplet([2,1,5,0,4,6]))
print(object.longestConsecutive([100,4,200,1,3,2]))
