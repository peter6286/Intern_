class Solution:
    # 经典二分 必背
    def binarysearch(self,nums,target):
        if not nums :
            return -1
        start,end = 0,len(nums)-1
        while start+1<end:
            mid = (start+end)//2
            if nums[mid]<target:
                start = mid
            elif nums[mid]==target:
                end = mid
            else:
                end = mid
        if nums[start]==target:
            return start
        if nums[end]==target:
            return end
        return -1


    # 447 · Search in a Big Sorted Array
    def searchBigSortedArray(self, reader, target):
        range_total = 1
        while reader.get(range_total-1)<target:
            range_total = range_total*2

        start,end = 0,range_total-1
        while start+1 < end:
            mid = (start+end)//2
            if reader.get(mid)<target:
                start=mid
            else:
                end = mid
        if reader.get(start)==target:
            return start
        if reader.get(end)==target:
            return end
        return -1


    #  460 · Find K Closest Elements

    # 确定中间的点走相反的方向
    def findClosestElements(self, arr, k, x):
        right = self.finupperclose(arr,x)
        left = right - 1
        res = []
        for _ in range(k):
            if self.isleftcloser(arr,x,left,right):
                res.append(arr[left])
                left -=1
            else:
                res.append(arr[right])
                right +=1
        return res

    # 找到最左边大于等于target的元素
    def finupperclose(self,arr,target):
        start,end = 0,len(arr)-1
        while start+1 < end:
            mid = (start+end)//2
            if arr[mid]>=target:    #mid >=target,mid符合条件往更做的寻找
                end = mid           #往更左的寻找，丢掉右边
            else:
                start = mid     # 大于等于target的元素在右边，丢掉左边
        # 因为要找最左的数所以先检测start
        if arr[start] >= target:
            return start
        if arr[end] >= target:
            return end
        return len(arr)

    def isleftcloser(self,arr,target,left,right):
        if left < 0 :
            return False
        if right >= len(arr):
            return True

        return target - arr[left] <= arr[right]-target



    # 658. Find K Closest Elements

    def findClosestElements2(self,arr,k,x):
        l, r = 0, len(arr) - 1

        # Find index of x or the closest val to x
        val, idx = arr[0], 0
        while l <= r:
            m = (l + r) // 2
            curDiff, resDiff = abs(arr[m] - x), abs(val - x)
            # |a - x| < |b - x|, or
            # |a - x| == |b - x| and a < b
            # 判断条件
            if (curDiff < resDiff or(curDiff == resDiff and arr[m] < val)):
                val, idx = arr[m], m

            if arr[m] < x: #距离target太小了舍去左边的部分
                l = m + 1
            elif arr[m] > x:    #距离target太大了舍去右边的部分
                r = m - 1
            else:
                break

        l = r = idx     #将左右的pointer都放在找到最近最右inedex上
        for _ in range(k - 1):
            if l == 0:  #如果是等于0的时候只能往前找
                r += 1          #如果是在队列的最后一位或者左边小于右边
            elif r == len(arr) - 1 or x - arr[l - 1] <= arr[r + 1] - x:
                l -= 1
            else:       #右边的小于左边的
                r += 1
        return arr[l:r + 1]


    # 585 · Maximum Number in Mountain Sequence

    def mountain_sequence(self, nums):
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return max(nums[left], nums[right])

    # LC 852. Peak Index in a Mountain Array
    def peakIndexInMountainArray(self, arr):
        if not arr:
            return -1
        start,end = 0,len(arr)-1
        while start+1 < end:
            mid = (start+end)//2
            if arr[mid]>arr[mid+1]:
                end = mid
            else:
                start = mid
        res = arr.index(max(arr[end],arr[start]))
        return res






object = Solution()
print(object.findClosestElements2([1,2,3,4,5],4,3))
print(object.peakIndexInMountainArray([0,10,5,2]))
