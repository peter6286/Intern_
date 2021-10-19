class Solution:
    #Implement strStr()
    # Input: haystack = "hello", needle = "ll"  Output: 2
    # Input: haystack = "aaaaa", needle = "bba" Output: -1
    # Input: haystack = "", needle = ""Output: 0
    def strStr(self, haystack, needle):
        stride = len(needle)
        haystack_length = len(haystack)
        total_step = haystack_length-stride+1
        if stride == 0:
            return 0
        for i in range(total_step):
            if haystack[i:i+stride] == needle:
                return i
        return -1


    # Longest Common Prefix 14
    # Input: strs = ["flower","flow","flight"] Output: "fl"
    #  Input: strs = ["dog","racecar","car"]  Output: ""

    def longestCommonPrefix(self, strs):
        # compares first letter of all words, then moves to next letter
        s = ""
        if len(strs)==0: #edge case, no elements in list
            return s
        elif len(strs)==1: #edge case, single element in list
            return strs[0]

        #word length of shortest word to prevent index out of range
        for a in range(len(min(strs))):
            #loops through each word in list, starting with second word
            for b in range(1, len(strs)):
                #compares nth character of first word to other words
                fist = strs[0][a]
                cmp = strs[b][a]
                if fist == cmp:
                    #only adds to pattern if nth character same up to the last word
                    if b==len(strs)-1: #要和后面的所有都比较完
                        fist
                        s += fist
                else: #exits when characters don't match
                    return s
        return s

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


object=Solution()
strs = ["flower","flow","flight"]
print(object.strStr("hello","ll"))
print(object.longestCommonPrefix(strs))
