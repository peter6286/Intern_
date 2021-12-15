class Solution:
    # 66. Plus One
    # Input: digits = [1,2,3]
    # Output: [1,2,4]
    # Input: digits = [4,3,2,1]
    # Output: [4,3,2,2]

    def plusOne(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:  #全是9的时候
            digits[length] = 0
            length -= 1
        if (length < 0):
            digits = [1] + digits    #全是9的时候长度小于0进位
        else:
            digits[length] += 1     #在前一位上进位
        return digits


object=Solution()
print(object.plusOne([4,3,2,1]))