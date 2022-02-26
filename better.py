def findday(s,k):
    weekdays = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    temp = weekdays.index(s)
    return weekdays[(k+temp)%7]


def balance(s):
    count,result,fraglength = 0,-1,0
    fragment = []
    for i in range(len(s)):
        if s[i].isupper():
            oppcase = s[i].lower()
            if oppcase in s[i:] or oppcase.lower() in fragment or oppcase.upper() in fragment:
                count +=1
                fragment.append(oppcase)
            else:
                count = 0
                if result != -1:
                    fraglength = result
                fragment = []
        elif s[i].islower():
            oppcase = s[i].upper()
            if oppcase in s[i:] or oppcase.lower() in fragment or oppcase.upper() in fragment:
                count +=1
                fragment.append(oppcase)
            else:
                count = 0
                if result != 1:
                    fraglength = result
                fragment = []
        if count > 1:
            result = count
        if fraglength < result and fraglength > 0:
            result = fraglength

    return result


def toggle(num):
    fivelist = []
    numlist = str(num)
    for i in range(len(numlist)):
        if numlist[i]=="5":
            print(numlist[:i]+numlist[i+1])
            fivelist.append(int(numlist[:i]+numlist[i+1:]))
    return max(fivelist)


def solution(A):
    dict = {}
    count = 0
    for item in A:
        if item not in dict:
            dict[item]=1
        else:
            dict[item]+=1
    print(dict)
    if len(dict) == 1:
        count = list(dict.values())[0]
    elif len(dict)%2==0:
        for i in dict:
            if dict[i]>=2:
                count+=dict[i]
    else:
        return len(dict)
    return count

A=[4,2,2,4,2]
B=[1,2,3,4]
C= [0,5,4,4,5,12]
print(findday("Wed",2))
print(balance("TacoCat"))
print(toggle(-5000))
print(solution(B))