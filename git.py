import math
'''
# 2
print("the floor value for 5.2 : ", math.floor(5.2))
print("the ceil value for 5.8 : ", math.ceil(5.72))

#3
var1,var2 = 2,3
var1,var2 = var2 ,var1
print(var1,var2)

# 4
name = input("please give me an name : ")
if name == 'peter':
    print("that is a nice name")
elif name == 'John Cleese' or name == 'Michael Palin':
    print('not a good name')
else:
    print('you have a nice name')

# 5
list1=[4.95,9.95,14.95,19.95,24.95]
list2=[]
list3=[]
for i in list1:
    m=i*(0.6)
    list3.append(i - m)
    list2.append(m)
print("Original price - new price  - Discounted amount")
for i in range(0,5):
    print("{} {:.2f} {:.2f}".format(list1[i],list2[i],list3[i]))

# 6
num1 = [ i for i in range(1,6)]
num2 = [ i for i in range(2,7)]
for i in range(len(num1)):
        print("{} {} {}".format(num1[i],num2[i],pow(num1[i],num2[i])))

# 7
import  random
guess = input("please give me an three digit number : ")
number = str(random.randrange(100,1000))
if guess == number:
    print("you have won $10,100")
count = 0
for item in guess:
    if item in number:
        count +=1
if count == 3:
    print("got the award of $3000")
elif count == 1:
    print("got the award of $1000")
else:
    print("do not have any award")

#8
numdict = {}
numlist = []
while True:
    num = int(input("give me the number"))
    if num == 0:
        break
    numlist.append(num)
    numdict[num] = 1 + numdict.get(num,0)
print("the largetst number is : " ,max(numlist))
print("the occurrence is : ", numdict[max(numlist)])

#
size = 6
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")


# 9
rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print(k, end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print(k, end=' ')
        k += 1
    print('')
    i -= 1

'''

res = []
digittoChar = {
"0" : ['0'],
"1" : ['1'],
"2" : ['2','a','b','c'],
"3" : ['3','d','e','f'],
"4" : ['4','g','h','i'],
"5" : ['5','j','k','l'],
"6" : ['6','m','n','o'],
"7" : ['7','q','p','r','s'],
"8" : ['8','t','u','v'],
"9" : ['9','w','x','y','z']}
for item in '1800flo':

    for key,value in digittoChar.items():
        if item in value:
            res.append(key)
print(res)