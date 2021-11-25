from collections import Counter


class Solution:
    # 704. Binary Search
    # Input: nums = [-1,0,3,5,9,12], target = 9   Output: 4
    # Input: nums = [-1,0,3,5,9,12], target = 2   Output: -1

    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    #35. Search Insert Position
    # Input: nums = [1,3,5,6], target = 5   Output: 2
    # Input: nums = [1,3,5,6], target = 2   Output: 1

    def searchInsert(self, nums, target):
        left=0
        right = len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid] < target:
                left = mid+1
            if nums[mid] > target:
                right = mid - 1
            else:
               return mid
        return left

    #278. First Bad Version
    #Input: n = 5, bad = 4     Output: 4
    #Input: n = 1, bad = 1    Output: 1
    ''''

    def firstBadVersion(self, n):
        left =0
        right = n
        while left<= right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid-1
            else :
                left = mid +1
        return left

    '''


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

    #977. Squares of a Sorted Array
    # Input: nums = [-4,-1,0,3,10]    Output: [0,1,9,16,100]
    # Input: nums = [-7,-3,2,3,11]    Output: [4,9,9,49,121]
    def sortsq(self,nums):
        result =[0] * len(nums)       #已经排好序
        left = 0
        right = len(nums)-1
        for index in range (len(nums)-1,-1,-1):  #从后往前的顺序
            if abs(nums[left])> abs(nums[right]):       #如果左边的大于右边的最后一位将它放在nums的最后一位
                result[index]=nums[left]**2
                left+=1
            else:
                result[index]=nums[right]**2
                right-=1
        return result


    #189. Rotate Array
    # Input: nums = [1,2,3,4,5,6,7], k = 3   Output: [5,6,7,1,2,3,4]
    # Input: nums = [-1,-100,3,99], k = 2    Output: [3,99,-1,-100]
    def rotate(self, nums, k):
        temp = [0] * len(nums)
        for i in range (len(nums)):
            temp[(i+k)%len(nums)]=nums[i]   #用%来达到对应的位置
        for j in range(len(nums)):
            nums[j]=temp[j]
        return nums


    #283. Move Zeroes
    # Input: nums = [0,1,0,3,12]   Output: [1,3,12,0,0]
    #Input: nums = [0]


    def moveZeroes(self, nums):
        l, r = 0, 0             #left找有0的index，right找替换点
        while r < len(nums):
            if nums[l] == 0:
                if nums[r] != 0:       #当不等于0时找到替换点换位
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
                else:
                    r += 1      #当right等于0的时候跳过
            else:
                l += 1    #left不等于0的时候
                r += 1
        return nums


    #167. Two Sum II - Input Array Is Sorted
    # Input: numbers = [2,7,11,15], target = 9    Output: [1,2]
    # Input: numbers = [2,3,4], target = 6       Output: [1,3]

    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l+=1            #往右缩近加大，往左移动减小
            elif s > r:
                r-=1
            else:
                return [l + 1, r + 1]


    # 344. Reverse String
    # Input: s = ["h","e","l","l","o"]   Output: ["o","l","l","e","h"]
    # Input: s = ["H","a","n","n","a","h"]  Output: ["h","a","n","n","a","H"]

    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left < right :
            s[left],s[right]=s[right],s[left]
            left,right = left+1,right-1

        return s


    # 557. Reverse Words in a String III
    # Input: s = "Let's take LeetCode contest"    Output: "s'teL ekat edoCteeL tsetnoc"
    # Input: s = "God Ding"      Output: "doG gniD"

    def reverseWords(self, s):
        tolist = s.split(" ")
        for i in range (len(tolist)):
            tolist[i] = tolist[i][::-1]
        return " ".join(tolist)


    #3. Longest Substring Without Repeating Characters
    # Input: s = "abcabcbb"   Output: 3
    # Input: s = "bbbbb"     Output: 1
    # Input: s = "pwwkew"   Output: 3

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int abcabcbb
        """
        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:    # If s[r] not in seen, we can keep increasing the window size by moving right pointer
                output = max(output,r-l+1)
            else:   # There are two cases if s[r] in seen
                if seen[s[r]] < l: # s[r] is not inside the current window, we can keep increase the window
                    output = max(output,r-l+1)
                else:   #s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output


    #567. Permutation in String
    # Input: s1 = "ab", s2 = "eidbaooo"  Output: true
    # Input: s1 = "ab", s2 = "eidboaoo"  Output: false
    def checkInclusion(self, s1, s2):
        window = len(s1)
        s1_c = Counter(s1)  #create a dictionary for s1
        print(s1_c)

        for i in range(len(s2)-window+1):       #how many time they need to get compared
            s2_c = Counter(s2[i:i+window])      #creare an dictioanry for s2
            print(s2_c)
            if s2_c == s1_c:       #compare two dictioary if they had the same pattern
                return True
        return False



    #876. Middle of the Linked List
    # Input: head = [1,2,3,4,5]    Output: [3,4,5]
    # Input: head = [1,2,3,4,5,6]   Output: [4,5,6]

    def middleNode(self, head):
        slow, fast = head, head

        while fast:

            fast = fast.next
            if fast:
                fast = fast.next
            else:
                # fast has reached the end of linked list
                # slow is on the middle point now
                break
            slow = slow.next
        return slow

    # 19. Remove Nth Node From End of List
    # Input: head = [1,2,3,4,5], n = 2   Output: [1,2,3,5]
    # Input: head = [1], n = 1      Output: []
    # Input: head = [1,2], n = 1    Output: [1]

    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head




    #733. Flood Fill
    #Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
    #Output: [[2,2,2],[2,2,0],[2,0,1]]
    #Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
    #Output: [[2,2,2],[2,2,2]]


    def floodFill(self, image, sr, sc, newColor):
        h, w = len(image), len(image[0])

        visited = set()

        def dfs(r, c, src_color, new_color):
            if r < 0 or c < 0 or r >= h or c >= w or (r, c) in visited or image[r][c] != src_color:
                # Reject for invalid coordination, repeated traversal, or different color
                return

            # update color
            image[r][c] = new_color

            # mark current coordination as visited
            visited.add((r, c))

            # DFS to 4-connected neighbors
            dfs(r - 1, c, src_color, new_color)
            dfs(r + 1, c, src_color, new_color)
            dfs(r, c - 1, src_color, new_color)
            dfs(r, c + 1, src_color, new_color)

        # ---------------------------------------------------------------------------

        dfs(sr, sc, image[sr][sc], newColor)

        return image

    # 695. Max Area of Island
    '''
    Input: grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                   [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    Output: 6
    '''
    # Input: grid = [[0,0,0,0,0,0,0,0]]    Output: 0

    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        maxArea = 0

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return 0

            maxArea = 1
            grid[i][j] = '#'  # this will act as visited set
            maxArea += dfs(grid, i + 1, j)
            maxArea += dfs(grid, i - 1, j)
            maxArea += dfs(grid, i, j + 1)
            maxArea += dfs(grid, i, j - 1)

            return maxArea

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(grid, i, j))

        return maxArea





object = Solution()
print(object.search([1,3,5,6],5))
print(object.searchInsert([1,3,5,6],5))
print(object.sortsq([-4,-1,0,3,10] ))
print(object.rotate([1,2,3,4,5,6,7],3))
print(object.moveZeroes([0,1,0,3,12]))
#print(object.removeNthFromEnd([node1,node2,node3],2))
print(object.reverseWords("Let's take LeetCode contest"))
print(object.lengthOfLongestSubstring("pwwkew"))
print(object.checkInclusion("ab","eidbaooo"))
print(object.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
