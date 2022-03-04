# Anagram Difference
# ea and ate are anagrams, so we would need to modify 0 characters.
# tea and toe are not anagrams, but we can modify 1 character in either
# string (o -> a or a-> o) to make them anagrams.
# act and acts are not anagrams and cannot be converted to anagrams
# because they contain different numbers of characters.

# a - an array of string
# b - an array of string
import collections
import re

def getMinimumDifference(a, b):
    s_count = collections.Counter(a)
    t_count = collections.Counter(b)
    count = 0
    for k, v in s_count.items():
        count += max(v - t_count[k], 0)
    return count

# Growth in 2 Dimension
def growth(steps):
    row = [0]*len(steps)
    col = [0]*len(steps)
    for i in range(0,len(steps)):   # 将row和col最小化然后求积
        temp = steps[i].split(" ")
        row[i] = int(temp[0])
        col[i] = int (temp[1])
    return min(row)*min(col)

# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
def maxarea(h,w,horizon,vertical):
    horizon.sort()
    vertical.sort()
    horizon = [0]+horizon + [h]
    vertical = [0] + vertical + [w] #也有可能是edge上形成的最大所以要加上两边
    max_h,max_w = 0,0
    for i in range(1,len(horizon)):
        max_h = max(max_h,abs(horizon[i-1]-horizon[i])) #用绝对距离算出最大的
    for i in range(1,len(vertical)):
        max_w = max(max_w,abs(vertical[i-1]-vertical[i]))
    return max_w * max_h


# prison break
def prison(h,w,vertical,horizon):
    horizon.sort()
    vertical.sort()
    max_h,max_w,current = 2,2,2     # 2 是base case移除任何一个bar都是2
    for i in range(0,len(horizon)-1):
        if (horizon[i]==horizon[i+1]-1) : #中间有东西挡住不能成为空隙所以得是连续的
            current = current + 1
            max_h = max(max_h,current)
        else:
            current = 2
    current = 2
    for i in range(0,len(vertical)-1):
        if (vertical[i]==vertical[i+1]-1):
            current = current + 1
            max_w = max(max_w,current)
        else:
            current = 2
    return (max_h*max_w)

# Identical Distribution
def identical(cardtype,packet):
    res = []
    if packet == 1:
        return 0
    for num in cardtype:
        if num% packet == 0:
            res.append(0)
        else:
            count = 0
            while num%packet!=0:
                num += 1
                count +=1
            res.append(count)
    return sum(res)

# counting closed path
def closed(num):
    sum = 0
    numdict={"0":1,"4":1,"6":1,"9":1,"8":2}
    for item in str(num):
        if item not in numdict:
            sum += 0
        else:
            sum += numdict[item]
    return sum


def gcd(d1,d2):
    if d2 == 0:
        return d1
    else:
        return gcd(d2,d1%d2)


def addfraction(n1,d1,n2,d2):
    res = []
    d3 = gcd(d1,d2)
    d3 = (d1*d2)/d3
    n3 = n1*(d3/d1)+n2*(d3/d2)
    common = gcd(n3,d3)
    d3 = d3/common
    n3 = n3/common
    r1,r2 = str(int(d3)),str(int(n3))
    return r2+ "/"+ r1


def reduece(expression):
    res = []
    for item in expression:
        a= re.split("[+ /]",item)
        res.append(addfraction(int(a[0]),int(a[1]),int(a[2]),int(a[3])))
    return res






a = ['abc','aaa']
b = ['bba','bbb']
print(getMinimumDifference(a,b))
print(growth(["1 4","2 3"]))
print(maxarea(3,2,[1,2,4],[1,2]))
print(identical([4,7,5,11,15],2))
print(closed(630))
print(addfraction(722,148,360,176))
print(reduece(["722/148+360/176","978/1212+183/183"]))
