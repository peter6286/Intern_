from collections import Counter

class solution:
    # 1636. Sort Array by Increasing Frequency
    def frequencySort(self, nums):
        # key: distinct number
        # value: frequency of number
        num_occ_dict = Counter(nums)

        # Sort number by pair of (frequency, and negative value)
        nums.sort(key=lambda x: (num_occ_dict[x], -x))
        # First, sort by frequency in increasing order,
        # then sort by value in decreasing order if frequency is the same.
        return nums

    # 1220. Count Vowels Permutation

    def countVowelPermutation(self, n):
        #@lru_cache(None)
        def dfs(i,lastchar):
            if i==n:            #base case 其他的按要求来就行
                return 1
            res = 0
            if lastchar =='a':
                res += dfs(i+1,'e')
            elif lastchar =='e':
                res += dfs(i+1,'a') + dfs(i+1,'i')
            elif lastchar =='i':
                res += dfs(i + 1, 'a') + dfs(i + 1, 'e') + dfs(i+1,'o') + dfs(i+1,'u')
            elif lastchar =='o':
                res += dfs(i + 1, 'u') + dfs(i + 1, 'i')
            elif lastchar == 'u':
                res += dfs(i + 1, 'a')

            return res%mod

        mod = 10**9+7
        return (dfs(1,'a')+dfs(1,'e')+dfs(1,'i')+dfs(1,'o')+dfs(1,'u'))%mod


    # 1389. Create Target Array in the Given Order
    def createTargetArray(self, nums, index):
        photo = []
        size = len(nums)
        for i in range(size):
            photo.insert(index[i],nums[i])
        return photo












object = solution()
print(object.frequencySort([1,1,2,2,2,3]))
print(object.countVowelPermutation(5))
print(object.createTargetArray([0,1,2,3,4],[0,1,2,1,2]))