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

print(findday("Wed",2))
print(balance("TacoCat"))
print(toggle(-5000))