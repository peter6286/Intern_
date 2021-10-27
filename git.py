def solution(A):
    temp =[]
    result=0
    for i in range (min(A),max(A)+1):
        temp.append(i)
    if (min(A) < 0):
        result = 1
        return  result
    for j in temp:
        if j not in A:
            result = j
            return  result
            exit()
        else:
            result = max(A)+1
    return result



    # write your code in Python 3.6
    return result

A=[1,3,6,4,1,2]

B=[-1,-3]
C=[1,2,3]
print(solution(C))