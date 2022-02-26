# Anagram Difference
# ea and ate are anagrams, so we would need to modify 0 characters.
# tea and toe are not anagrams, but we can modify 1 character in either
# string (o -> a or a-> o) to make them anagrams.
# act and acts are not anagrams and cannot be converted to anagrams
# because they contain different numbers of characters.

# a - an array of string
# b - an array of string
import collections

def getMinimumDifference(a, b):
    differences_array = []
    for i,word in enumerate(a):
        if len(word) != len(b[i]):
            differences_array.append(-1)    # 如果长度不想等直接返回负一
            continue
        difference = 0

        a_freq = dict(collections.Counter(a[i]))
        b_freq = dict(collections.Counter(b[i]))
        print(a_freq)
        print(b_freq)

        for letter,value in a_freq.items():
            if letter in b_freq:
                difference += abs(a_freq[letter]-b_freq[letter])

            else:
                difference += value     # 如果没有这个字母添加这个字母出现的次数就是difference

        differences_array.append(difference)

    return differences_array

def growth(steps):
    row_sets = []
    col_sets = []
    for step in steps:
        row_bound, col_bound = map(int, step.split(' '))
        row_range = list(range(0, row_bound))
        col_range = list(range(0, col_bound))

        row_sets.append(set(row_range))
        col_sets.append(set(col_range))

    row_intersection = set.intersection(*row_sets)
    col_intersection = set.intersection(*col_sets)

    cells = len(row_intersection) * len(col_intersection)

    return cells


a = ['a','jk','abb','mn','abc']
b = ['bb','kj','bbc','op','def']
print(getMinimumDifference(a,b))
print(growth(["1 4","2 3","4 1"]))
