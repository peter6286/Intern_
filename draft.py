


def doblev (nums):
    #拿到number = [1,3,7]
    for i in range (len(nums)):
        nums[i] = nums[i]*2 #在每个index上乘二然后放回原位
    return nums


number = [1,3,7 ] #这是一个名为number 的 list
result = doblev(number) #把list放入这个function对应上面的 def doblev (nums):
#print(result)#把结果打印出来


def isPrime(n):
   if n <= 1 or n % 1 > 0:
      return False
   for i in range(2, n//2):
      if n % i == 0:
         return False
   return True



#print(isPrime(67))


def canConstruct( ransomNote, magazine):
    for i in set(ransomNote):
        if magazine.count(i) < ransomNote.count(i):
            return False
    return True
#print(canConstruct("aa","aab"))
ran = "aab"
print(set(ran))
