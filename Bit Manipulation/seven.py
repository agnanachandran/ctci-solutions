#
# 5.7
# An array A[1 n] contains all the integers from 0 to n except for one number which is missing In this problem, we cannot access an entire integer in A with a single opera- tion The elements of A are represented in binary, and the only operation we can use to access them is “fetch the jth bit of A[i]”, which takes constant time Write code to find the missing integer Can you do it in O(n) time?

def log_two(num):
    power = 0
    while num != 1:
        num /= 2
        power += 1
    #print power
    return power


def slow_find_missing_int(arr):
    if not arr: return
    N = len(arr)
    seen = set()
    power = log_two(N) + 1
    for i in arr:
        total = 0
        for j in xrange(power):
            bit = get_bit(i, j)
            if bit:
                total += 2 ** j
        seen.add(total)
    for i in range(N):
        if i not in seen:
            print i

def fast_find_missing_int(arr):
    if not arr: return
    idx = 0
    n = len(arr)
    nums = set(arr)
    power = log_two(n)
    chosen = [x for x in arr]
    final_num = 0
    while idx <= power:
        evens = [x for x in chosen if get_bit(x, idx) == 0]
        odds = [x for x in chosen if get_bit(x, idx) == 1]
        print evens, odds
        if len(odds) >= len(evens):
            # even missing
            chosen = evens
        else:
            final_num += 2 ** idx
            chosen = odds
        idx += 1
    print final_num

def get_bit(i, j):
    return ((1 << j) & i) > 0

fast_find_missing_int([0, 2, 4, 3, 5, 6])
