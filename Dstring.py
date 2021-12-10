import collections
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

    # 290. Word Pattern
    # Input: pattern = "abba", s = "dog cat cat dog"     Output: true
    # Input: pattern = "abba", s = "dog cat cat fish"    Output: false
    # Input: pattern = "aaaa", s = "dog cat cat dog"     Output: false

    def wordPattern(self, pattern, s):
        pattern_dict = {}
        str_dict = {}
        str_word = s.split()
        if len(pattern) != len(str_word):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = i
            if str_word[i] not in str_dict:
                str_dict[str_word[i]] = i
        for i in range(len(pattern)):   #比较dictionary里的index是否是一样的
            if pattern_dict[pattern[i]] != str_dict[str_word[i]]:
                return False
        return True


    # 242. Valid Anagram
    # Input: s = "anagram", t = "nagaram"    Output: true
    # Input: s = "rat", t = "car"            Output: false

    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for item in s:
            if item not in s_dict:
                s_dict[item] = 1
            else:
                s_dict[item] += 1
        for item in t :
            if item not in t_dict:
                t_dict[item] = 1
            else:
                t_dict[item] += 1
        if s_dict == t_dict:
            return True
        else:
            return False


    # 49. Group Anagrams
    # Input: strs = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    #Input: strs = [""]
    #Output: [[""]]

    def groupAnagrams(self, strs):
        d = {}
        ans = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = [word]
            else:
                d[sorted_word].append(word)

        for key in d:
            ans.append(d[key])

        return ans


    # 179. Largest Number
    # Input: nums = [10,2]   Output: "210"
    # Input: nums = [3,30,34,5,9]    Output: "9534330"
    # Input: nums = [1]      Output: "1"
    def largestNumber(self, nums):
        def compare(n1, n2):
            num1 = str(n1)+str(n2)
            num2 = str(n2)+str(n1)
            return num1 > num2

        for i in range(len(nums), 0, -1):  #bubble sort 每个确定一个最高位
            for j in range(i - 1):          # 相互比较的小循环让item到对应的位置
                if not compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return str(int("".join(map(str, nums))))

    # 316. Remove Duplicate Letters
    # Input: s = "bcabc"     Output: "abc"
    # Input: s = "cbacdcbc"    Output: "acdb"
    # 不会


    def removeDuplicateLetters(self, s):
        stack = []
        seen = set()
        last_occurance = {}
        for i in range(len(s)):
            last_occurance[ s[i] ] = i

        print(last_occurance)

        for i, ch in enumerate(s):
            print(i)
            print(ch)
            if( ch in seen ):
                continue
            else:
            # 3 temp1 = stack[-1]
                while( stack and stack[-1] > ch and last_occurance[stack[-1]] > i ):
                    a=stack[-1]
                    b=last_occurance[stack[-1]]
                    removed_char = stack.pop()
                    seen.remove(removed_char)
                seen.add(ch)
                stack.append(ch)
        # print(stack)
        return ''.join(stack)


    # 168. Excel Sheet Column Title
    # Input: columnNumber = 1     Output: "A"
    # Input: columnNumber = 28    Output: "AB"
    # Input: columnNumber = 701   Output: "ZY"

    # A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
    # B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
    # .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
    # .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
    # .   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
    # Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26


    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]   #创建A-Z的数组
        result = []
        print(capitals)
        while num > 0:
            result.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)



    # 171. Excel Sheet Column Number
    # Input: columnTitle = "A"    Output: 1
    # Input: columnTitle = "AB"   Output: 28
    # Input: columnTitle = "ZY"   Output: 701
    def convertToTitle2(self,s):
        p = 1
        summ = 0
        for i in s[::-1]:
            #print(ord(i))
            summ += p * (ord(i) - 64)  # -ord(A)+1 像十进制一样进位
            p *= 26

        return summ


    # 13. Roman to Integer
    # Input: s = "III"    Output: 3
    # Input: s = "IV"     Output: 4
    # Input: s = "IX"     Output: 9
    # Input: s = "LVIII"  Output: 58
    def romanToInt(self, s):
        res, prev = 0, 0
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        print(s[::-1])          #大的应该在前面
        for i in s[::-1]:  # rev the s
            if dict[i] >= prev:
                res += dict[i]  # sum the value iff previous value same or more
            else:
                res -= dict[i]  # substract when value is like "IV" --> 5-1, "IX" --> 10 -1 etc
            prev = dict[i]
        return res


    #12. Integer to Roman
    # Input: num = 3    Output: "III"
    # Input: num = 4    Output: "IV"
    # Input: num = 9    Output: "IX"
    # Input: num = 58   Output: "LVIII"

    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ""
        for i, v in enumerate(values):
            res += (num//v) * numerals[i] #除后不是小数才可以继续除进入输出
            num %= v  #比大的数除还是自己本身
        return res




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


    # 395. Longest Substring with At Least K Repeating Characters
    # Input: s = "aaabb", k = 3      Output: 3
    # Input: s = "ababbc", k = 2     Output: 5

    def longestSubstring(self, s, k):
        cnt = collections.Counter(s)    #给s里的字母制作dictionary
        print(cnt)
        st = 0  #substring开始的点
        maxst = 0
        for i, c in enumerate(s):
            if cnt[c] < k:  #如果字母少于k的话输出目前长度比较
                maxst = max(maxst, self.longestSubstring(s[st:i], k))
                st = i + 1  #将开始点移到目前的点上
        return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))



    # 125. Valid Palindrome
    # Input: s = "A man, a plan, a canal: Panama"     Output: true
    # Input: s = "race a car"          Output: false
    # Input: s = " "                   Output: true

    def isPalindrome1(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum(): #如果left不是一个alphabet
                l += 1
            elif not s[r].isalnum(): #如果right不是一个alphabet
                r -= 1
            else:
                if s[l].lower() != s[r].lower():  #如果左右两边的alphabet相同
                    return False
                else:
                    l += 1
                    r -= 1
        return True


    # 5. Longest Palindromic Substring
    # Input: s = "babad"     Output: "bab"
    # Input: s = "cbbd"      Output: "bb"
    # Input: s = "a"         Output: "a"
    # Input: s = "ac"        Output: "a"

    def longestPalindrome(self, s):
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome.
        dp = [[False] * n for _ in range(n)]  #制作全是false的table，会是true如果是palindrome

        ans = ''
        # every string with one character is a palindrome
        for i in range(n):    #字母本身是一个substring所以可以设置为 ture
            dp[i][i] = True
            ans = s[i]

        maxLen = 1
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                # palindrome condition
                if s[start] == s[end]:  #如果头和尾巴是相同的
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start + 1][end - 1]: #头和尾巴中间刚好是差1个字母或者是true
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end + 1]

        return ans



    # 283. Move Zeroes
    # Input: nums = [0,1,0,3,12]      Output: [1,3,12,0,0]
    # Input: nums = [0]               Output: [0]

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



    #376. Wiggle Subsequence
    # 不会


    #9. Palindrome Number
    # Input: x = 121     Output: true
    # Input: x = -121    Output: false
    # Input: x = 10      Output: false
    # Input: x = -101    Output: false
    def isPalindrome(self, x):
        num=str(x)
        left=0
        right=len(num)-1
        while left < right:
            if num[left]==num[right]:
                left+=1
                right-=1
            else:
                return False
        return True

    #131. Palindrome Partitioning
    # Input: s = "aab"        Output: [["a","a","b"],["aa","b"]]
    # Input: s = "a"          Output: [["a"]]

    def partition(self, s):
        def dfs(s, path , res):
            if not s:
                res.append(path)
            for i in range(1, len(s)+1):
                if self.isPalindrome(s[:i]):
                    dfs(s[i:], path+[s[:i]], res)
        res = []
        dfs(s, [], res)
        return res


    # 20. Valid Parentheses
    # Input: s = "()"       Output: true
    # Input: s = "()[]{}"   Output: true
    # Input: s = "(]"       Output: false
    # Input: s = "([)]"     Output: false
    # Input: s = "{[]}"     Output: true

    def isValid(self, s):
        d = {"(": ")", "[": "]", "{": "}"}   #制作dictionary map对应的的符号
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:    #如果stack里面没有东西或者map的东西不对
                return False
        return len(stack) == 0

    # 22. Generate Parentheses
    # Input: n = 3
    # Output: ["((()))","(()())","(())()","()(())","()()()"]
    # Input: n = 1
    # Output: ["()"]


    # only add open paranthesis if open < n
    # only add a closing paranthesis if closed < open
    # valid iff open == closed == n

    def generateParenthesis(self, n):
        res=[]
        stack=[]
        def dfs(openn,closen):
            if openn==closen==n:
                res.append("".join(stack))
                return
            if openn < n:
                stack.append("(")
                dfs(openn+1,closen)
                stack.pop()
            if openn > closen:
                stack.append(")")
                dfs(openn,closen+1)
                stack.pop()
        dfs(0,0)
        return res


    # 241. Different Ways to Add Parentheses
    # Input: expression = "2-1-1"     Output: [0,2]
    # Input: expression = "2*3-4*5"   Output: [-34,-14,-10,-10,10]

    def diffWaysToCompute(self, expression):
        def dp(s):
            res = []
            for i in range(len(s)):
                if '+' not in s and '-' not in s and '*' not in s:
                    return [int(s)]
                if s[i] in ('+', '-', '*'):     #查看是否在里面
                    L1 = dp(s[:i])
                    L2 = dp(s[i + 1:])
                    if s[i] == '+':         #把左边右边相加相减后的值加起来
                        for x in L1:
                            for y in L2:
                                res.append(x + y)
                    elif s[i] == '-':
                        for x in L1:
                            for y in L2:
                                res.append(x - y)
                    else:
                        for x in L1:
                            for y in L2:
                                res.append(x * y)
            return res
        return dp(expression)








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
print(object.wordPattern("abba","dog cat cat dog"))
print(object.isAnagram("rat","car"))
print(object.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(object.largestNumber([3,30,34,5,9]))
print(object.removeDuplicateLetters("cbacdcbc"))
print(object.convertToTitle(28))
print(object.convertToTitle2("AB"))
print(object.romanToInt("IX"))
print(object.intToRoman(58))
print(object.lengthOfLongestSubstring("abcabcbb"))
print(object.isPalindrome(1001))
print(object.partition("aab"))
print(object.longestSubstring("ababbc",2))
print(object.longestPalindrome("baabd"))
print(object.moveZeroes([0,1,0,3,12]))
print(object.generateParenthesis(3))
print(object.diffWaysToCompute("2-1-1"))