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

    # 58. Length of Last Word
    # Input: s = "Hello World" Output: 5
    # Input: s = "   fly me   to   the moon  " Output: 4

    def lengthOfLastWord(self, s):
        wordlist = s.split() #split 以后变为list忽略空格
        #print(wordlist)
        if wordlist:
            return len(wordlist[-1])
        return 0

    # 387. First Unique Character in a String
    # Input: s = "leetcode"  Output: 0
    # Input: s = "loveleetcode"  Output: 2

    def firstUniqChar(self, s):
        d = {}
        index = -1
        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        return index

    # 383. Ransom Note
    # Input: ransomNote = "a", magazine = "b"  Output: false
    # Input: ransomNote = "aa", magazine = "ab" Output: false
    # Input: ransomNote = "aa", magazine = "aab" Output: true

    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

    # 344. Reverse String
    # Input: s = ["h","e","l","l","o"]    Output: ["o","l","l","e","h"]
    # Input: s = ["H","a","n","n","a","h"]  Output: ["h","a","n","n","a","H"]

    def reverseString(self, s):
        # one points to head position, the other points to tail position
        left, right = 0, len(s) - 1

        # reverse string by two pointers
        while left < right:
            s[left], s[right] = s[right], s[left]

            left, right = left + 1, right - 1
        return s

    #151. Reverse Words in a String
    #Input: s = "the sky is blue"   Output: "blue is sky the"
    # Input: s = "  hello world  "  Output: "world hello"

    def reverseWords(self, s):
        str = " "
        split2list =s.split()
        rev = split2list[::-1]
        tostr = str.join(rev)
        result = tostr.strip()
        return result


    #345. Reverse Vowels of a String
    # Input: s = "hello"   Output: "holle"
    #Input: s = "leetcode"   Output: "leotcede"

    
    def reverseVowels(self, s):
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowels:   #往前开始不是vowels就往前一位
                i += 1
                continue
            if s[j] not in vowels:  #往后开始不是vowels就往后一位
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]  #如果是vowels的话换位置
            i += 1
            j -= 1

        return ''.join(s)

    # 205. Isomorphic Strings
    # Input: s = "egg", t = "add"    Output: true
    # Input: s = "foo", t = "bar"    Output: false
    # Input: s = "paper", t = "title"  Output: true

    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:  #判断pattern有没有形成
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]   #在dicationary给对应的值
            t2s[t[i]] = s[i]
        return True








object=Solution()
strs = ["flower","flow","flight"]
print(object.strStr("hello","ll"))
print(object.longestCommonPrefix(strs))
print(object.lengthOfLastWord("  Fly me to the moon"))
print(object.firstUniqChar("eetcode"))
print(object.canConstruct("aa","aab"))
print(object.reverseString(["h","e","l","l","o"]))
print(object.reverseWords("the sky is blue"))
print(object.reverseVowels("hello"))
print(object.isIsomorphic("egg","add"))
print(object.isIsomorphic("foo","bar"))
