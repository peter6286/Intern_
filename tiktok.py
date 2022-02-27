def tonum(rom):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    num = 0
    for i, c in enumerate(rom):
        if i + 1 < len(rom) and dict[c] < dict[rom[i + 1]]:
            num -= dict[c]
        else:
            num += dict[c]
    return num

def sortAncestral(names):
    names = [name.split() for name in names]
    for name in names:
        name.append(tonum(name[1]))
    names.sort(key=lambda x: (x[0], x[-1]))
    for i, name in enumerate(names):
        names[i] = ' '.join(name[:2])
    return names


def count3d(n):
    MOD = int(1e9 + 7)
    if n == 1:
        return 2

    MOD = int(1e9 + 7)

    f = [1, 2]

    # partial, one orientation, top layer is vertical
    # p(n) = f(n - 2) + p(n - 1)
    p = 0  # p(1)

    for i in range(n - 1):
        f = [f[1], (5 * f[0] + 2 * f[1] + 4 * p) % MOD]
        p = (p + f[0]) % MOD
        print(f)

    return f[1]


def cnt(s, l, r):
        # 0-indexed
        l -= 1
        r -= 1

        bar = [i for i, c in enumerate(s) if c == '|']
        #star = [r_bar - l_bar - 1 for l_bar, r_bar in pairwise(bar)]

        # build BIT
        bit = [0] * (1 + len(star))
        for i, cnt in enumerate(star, 1):
            while i < len(bit):
                bit[i] += cnt
                i += i & -i
                # query
        l = min(bisect_left(bar, l), len(bar) - 1)  # closest index >= l
        r = max(bisect_right(bar, r) - 1, 0)  # closest index <= r
        if l >= r:
            return 0
        else:
            res1, res2, res = 0, 0, 0
            while r > 0:
                res1 += bit[r]
                r -= r & -r

            while l > 0:
                res2 += bit[l]
                l -= l & -l
            return res1 - res2


def minSubArrayLen( target, nums):
    l = 0
    s = 0
    smallest_len = len(nums) + 1

    for r, n in enumerate(nums):
        s += n
        while s >= target:
            smallest_len = min(smallest_len, r - l + 1)
            s -= nums[l]
            l += 1

    return smallest_len if smallest_len <= len(nums) else 0

def reachingPoints(sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx:
                return (ty - sy) % sx == 0
            if ty == sy:
                return (tx - sx) % sy == 0

            if tx > ty:
                tx %= ty  # subtract until tx < ty
            elif tx < ty:
                ty %= tx
            else:
                # tx != sx or ty != sy
                return False

        return False



class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        x, v = self.stack.pop()
        if self.stack:
        	# inherit the value to add
            self.stack[-1][-1] += v
        return x + v

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        k = min(k, len(self.stack))
        # maintain the value on the top
        self.stack[k - 1][1] += val



names = ["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]
print(sortAncestral(names))
print(count3d(100))  # 828630254
#print(cnt(s, 1, 6))
print(minSubArrayLen(7,[2, 1, 5, 2, 3, 2]))
