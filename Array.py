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
        if len(nums)<3:
            return len(nums)
        len_ = 2   # 替换的点
        for i in range (2,len(nums)):
            if nums[i] != nums[len_-2]: #检查和前面的两个点是否相同
                nums[len_] = nums[i]
                len_ +=1
        return len_

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
                area = max(area,width*height[right])
                right-=1
        return  area


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



    #334. Increasing Triplet Subsequence
    #Input: nums = [1,2,3,4,5]    Output: true
    #Input: nums = [5,4,3,2,1]    Output: false
    #Input: nums = [2,1,5,0,4,6]   Output: true

    def increasingTriplet(self,nums):
        first = second = float('inf')   #将第一个和第二个设置为无限
        for n in nums:
            if n <= first:          #如果比之前的小就重新设置
                first = n
            elif n <= second:       #接下来重新设置第二个
                second = n
            else:                   #出现比第一个和第二个大的数
                return True
        return False


    #128. Longest Consecutive Sequence
    # Input: nums = [100,4,200,1,3,2]   Output: 4
    # Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9
    def longestConsecutive(self, nums):
        nums.sort()
        longest, cur_longest = 0, min(1, len(nums))
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] : #如果前后index刚好都相等
                continue
            if nums[i] == nums[i - 1] + 1:      #目前的index item加1后刚刚好相等
                cur_longest += 1
            else:
                longest, cur_longest = max(longest, cur_longest), 1  #输出目前最长的
        return max(longest, cur_longest)

    # 287. Find the Duplicate Number
    # Input: nums = [1,3,4,2,2]       Output: 2
    # Input: nums = [3,1,3,4,2]       Output: 3
    # Input: nums = [1,1]             Output: 1


    def findDuplicate(self, nums):
        nums_dict = {}
        for item in nums :
            if item not in nums_dict:
                nums_dict[item]=1
            else:
                return item

    # 289. Game of Life

    # Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    # Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    # Input: board = [[1,1],[1,0]]
    # Output: [[1,1],[1,1]]
    def gameOfLife(self, board):
            """
            Do not return anything, modify board in-place instead.
            """
            ## RC ##
            ## APPRAOCH : IN-PLACE MANIPULATION ##
            ##  when the value needs to be updated, we donot just change  0 to 1 / 1 to 0
            ##  but we do in increments and decrements of 2. (table explains)
            ##   previous value state change  current state   current value
            ##   0              no change     dead            0
            ##   1              no change     live            1
            ##   0              changed (+2)  live            2
            ##   1              changed (-2)  dead            -1

            ## TIME COMPLEXITY : O(MxN) ##
            ## SPACE COMPLEXITY : O(1) ##

            directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

            for i in range(len(board)):
                for j in range(len(board[0])):
                    live = 0  # live neighbors count
                    for x, y in directions:  # check and count neighbors in all directions
                        if (i + x < len(board) and i + x >= 0) and (j + y < len(board[0]) and j + y >= 0) and abs(
                                board[i + x][j + y]) == 1:
                            live += 1
                    if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                        board[i][j] = -1
                    if board[i][j] == 0 and live == 3:  # Rule 4
                        board[i][j] = 2
            for i in range(len(board)):
                for j in range(len(board[0])):
                    board[i][j] = 1 if (board[i][j] > 0) else 0
            return board



    # 53. Maximum Subarray
    # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.

    # Input: nums = [5,4,-1,7,8]
    # Output: 23

    def maxSubArray(self, nums):
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            tempsum = curSum + num  # 到这个点为止最优的所有index的合
            curSum = max(num, tempsum)  # 比较是加上num后大（有负数）还是原本数字大。取value大的为新的current
            maxSum = max(maxSum, curSum)  # 更新最优的总数

        return maxSum


    # 209. Minimum Size Subarray Sum
    # Input: target = 7, nums = [2,3,1,2,4,3]     Output: 2
    # Input: target = 4, nums = [1,4,4]      Output: 1
    # Input: target = 11, nums = [1,1,1,1,1,1,1,1]   Output: 0

    def minSubArrayLen(self, target, nums):
        if len(nums) == 0: return 0
        i, j = 0, 0
        c, t = float("inf"), nums[0]
        while j <= len(nums) - 1:
            if t < target:      #如果比target小的话继续移动j的pointer往右边拓展
                j += 1
                if j <= len(nums) - 1: #小于最后的一个index
                    t += nums[j]
            elif t >= target:   #如果比target 等于或大的话移动i的pointer
                c = min(j - i + 1, c)          #看最短的长度
                t -= nums[i]
                i += 1
        return c if c != float("inf") else 0

    # 238. Product of Array Except Self
    # Input: nums = [1,2,3,4]    Output: [24,12,8,6]
    # Input: nums = [-1,1,0,-3,3]    Output: [0,0,9,0,0]

    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


    # 152. Maximum Product Subarray
    # Input: nums = [2,3,-2,4]     Output: 6
    # Input: nums = [-2,0,-1]      Output: 0

    # 1. Edge Case : Negative * Negative = Positive
    # 2. So we need to keep track of minimum values also, as they can yield maximum values.

    def maxProduct(self, nums): #因为有负负得正情况所以需要curr_min记录
        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:   #curr_max 记录循环到的地方的时候的最大值
            curr_min = min(prev_max * num, prev_min * num, num)
            curr_max = max(prev_max * num, prev_min * num, num)
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max


    #228. Summary Ranges
    # Input: nums = [0,1,2,4,5,7]      Output: ["0->2","4->5","7"]
    # Input: nums = [0,2,3,4,6,8,9]    Output: ["0","2->4","6","8->9"]
    # Input: nums = []                 Output: []
    # Input: nums = [-1]               Output: ["-1"]


    def summaryRanges(self,nums):
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        res = []
        curr=[]
        curr.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] - curr[-1] == 1:   #刚好和前面的差1
                curr.append(nums[i])
            else:   #如果不是差1的时候
                if len(curr) > 1:   #将目前已经形成range的curr先输出进result
                    res.append(str(curr[0]) + '->' + str(curr[-1]))
                    curr = []  #清空后最新的将单个放入
                    curr.append(nums[i])
                else:
                    res.append(str(curr[-1]))#将单个element放入result
                    curr = []
                    curr.append(nums[i])
            if i == len(nums) - 1 and len(curr) == 1: #将剩下的单个元素的放入
                res.append(str(nums[-1]))
            if i == len(nums) - 1 and len(curr) > 1: #将range放入
                res.append(str(curr[0]) + '->' + str(curr[-1]))
        return res


    # 88. Merge Sorted Array
    # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # [1,2,2,3,5,6]
    #  nums1 = [1], m = 1, nums2 = [], n = 0
    # [1]
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:   #使用merger sort
            if nums1[m-1] > nums2[n-1]:  #更新后的长度是m+n，所以更新的index从nums1[m+n-1]开始
                nums1[m+n-1] = nums1[m-1] #从大到小开始sort
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        while n > 0:        #检查有没有漏的
            nums1[n-1] = nums2[n-1]
            n -= 1

    # 75. Sort Colors
    # We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
    # Input: nums = [2,0,2,1,1,0]     Output: [0,0,1,1,2,2]
    # Input: nums = [2,0,1]           Output: [0,1,2]
    # Input: nums = [0]               Output: [0]

    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:   #用white做pointer
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]  #红色和白色跟随着加上去，互相更换位置
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white] #如果是蓝色的话换位置，讲蓝色换到最后然后减1
                blue -= 1

        return nums


    #283. Move Zeroes
    # Input: nums = [0,1,0,3,12]    Output: [1,3,12,0,0]
    # Input: nums = [0]             Output: [0]
    def moveZeroes(self, nums):
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


    # 324. Wiggle Sort II
    # Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]
    # Input: nums = [1,5,1,1,6,4]     Output: [1,6,1,5,1,4]
    # Input: nums = [1,3,2,2,3,1]     Output: [2,3,1,3,1,2]
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2])       #nums[1::2] 奇数位的index
        print(nums[::2])            #nums[::2] 偶数位的index
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]  #nums里的偶数index放排序后中间较小的index
        return nums                                                  #nums里的奇数index放排序后中间较大的index

    def findDisappearedNumbers(self, nums):
        dict = {}
        res = []
        for i in range(1,len(nums)+1):
            dict[i]=0
        print(dict)
        for item in nums:
            dict[item]+=1
        for key,value in dict.items():
            if dict[key] == 0:
                res.append(key)
        return res

    def findDisappearedNumbers2(self, nums):
        for n in nums:
            i = abs(n)-1        #让数字到对应的index上
            nums[i] = -1 *abs(nums[i])
        res = []
        for i,n in enumerate(nums):
            if n > 0:   #将不是负的元素(不在range中的元素)放入队列中
                res.append(i+1)
        return res


    # 1288. Remove Covered Intervals
    # Input: intervals = [[1,4],[3,6],[2,8]]
    # Output: 2
    # Input: intervals = [[1,4],[2,3]]
    # Output: 1
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda i:(i[0],-i[1]))
        res = [intervals[0]]
        for l,r in intervals[1:]:
            prevL,prevR = res[-1]
            if prevL <= l and prevR >= r:
                continue
            res.append([l,r])
        return len(res)

    def minDominoRotations(self, tops, bottoms):
       for target in [tops[0],bottoms[0]]: #让其中一个做target
           missingT,missingB=0,0
           for i,pair in enumerate(zip(tops,bottoms)):
               top,bottom = pair
               if not (top == target or bottom == target):
                    break
               if top!= target:missingT +=1
               if bottom != target:missingB+=1
               if i == len(tops)-1:
                    return min(missingT,missingB)
       return -1


    # 598. Range Addition II
    # Input: m = 3, n = 3, ops = [[2,2],[3,3]]
    # Output: 4
    # Explanation: The maximum integer in M is 2,
    # and there are four of it in M. So return 4.
    # Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2]
    # ,[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
    # Output: 4
    def maxCount(self, m, n, ops):
        if len(ops) == 0:
            return m * n
        row = [0] * len(ops)
        col = [0] * len(ops)
        for i in range(0, len(ops)):
            row[i] = int(ops[i][0])
            col[i] = int(ops[i][1])
        return min(row) * min(col)




    # 680. Valid Palindrome II


    def validPalindrome(self, s):
        if s is None:
            return False
        left, right = self.finddifference(s, 0, len(s) - 1)
        if left >= right:  # base case 本来就是palindrome
            return True
        return self.ispalindrome(s, left + 1, right) or self.ispalindrome(s, left, right - 1)

    def ispalindrome(self, s, left, right):
        left, right = self.finddifference(s, left, right)
        return left >= right

    def finddifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right


    # 1. Two Sum
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]


    def twoSum(self, nums, target):
        h = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if n not in h:   # n得到余数如果再出现就代表找到了
                h[remainder] = i
            else:
                return [h[remainder], i]











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
print(object.increasingTriplet([5,4,6,3,2,1]))
print(object.increasingTriplet([2,1,5,0,4,6]))
print(object.longestConsecutive([100,4,200,1,3,2]))
print(object.findDuplicate([1,1]))
print(object.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
print(object.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(object.minSubArrayLen(7,[2,3,1,2,4,3]))
print("aye")
print(object.productExceptSelf([1,2,3,4]))
print(object.maxProduct([-2,0,-1]))
print(object.summaryRanges([0,2,3,4,6,8,9]))
print(object.sortColors([0,1,2]))
print(object.wiggleSort([1,5,1,1,6,4]))
print(object.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(object.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(object.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2]))
print(object.validPalindrome("abcdba"))
print(object.two_sum5([2,7,11,15],24))