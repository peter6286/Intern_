

def solution(S, K):
    date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.index(S)
    temp = day + K
    newdate = temp % len(date)
    result = date[newdate]
    return result


def getmax (num):
    temp = str(num)
    #print(temp)
    largest = 0
    x_lst = [int(num) for num in str(num)]
    indexoffive = [x_lst.index(5)]

    for i in indexoffive:
        temp2 = int(str(temp[:i]+temp[i+1:]))
        if temp2 > largest:
            largest = temp2
    return largest
date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
print(solution('MON',2))
print(getmax(15958))
x=15958
x_lst = [int(x) for x in str(x)]
print(x_lst)
print([x_lst.index(5)])
