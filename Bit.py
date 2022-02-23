class Solution:

    # ^= 异位操作(XOR)

    #389. Find the Difference
    # s = abc
    # t = cabx
    #
    # if we take XOR of every character. all the n character of s "abc" is similar to n character of t "cab". So, they will cancel each other.
    # And we left with our answer.
    #
    # s =   abc
    # t =   cbax
    # ------------
    # ans -> x
    # -----------
    def findTheDifference(self, s, t):
        c = 0
        for cs in s:
            #print(ord(cs))
            c ^= ord(cs)  # ord is ASCII value
        print(c)
        for ct in t:
           # print(ord(ct))
            c ^= ord(ct)
        print(c)
        return chr(c)  # chr = convert ASCII into character
    # 136. Single Number
    # Input: nums = [2,2,1]
    # Output: 1
    # Input: nums = [4,1,2,1,2]
    # Output: 4


    def singleNumber(self, nums):
        dict = {}
        for item in nums:
            if item not in dict:
                dict[item]=1
            else:
                dict[item]+=1
        for ele in dict:
            if dict[ele] ==1:
                return ele

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res




    def maxProduct(self, words):
        mask, ans = [0] * len(words), 0
        for i, word in enumerate(words):
            for ch in word:
                mask[i] |= 1 << (ord(ch) - ord('a'))       # hash the word into integer
            for j in range(i):  #循环过滤每个元素
                if not mask[i] & mask[j]:       # 判断有没有相同的char在word[i]和word[j]中
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans




object=Solution()
print(object.findTheDifference("abc","cabx"))
print(object.singleNumber([1]))
print(object.singleNumber2([4,1,2,1,2]))
print(object.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))