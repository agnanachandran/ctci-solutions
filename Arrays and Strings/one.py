#
# 1.1
#
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures? (arrays/lists are allowed, apparently)
#

def all_unique_with_bit_vector_assume_ascii(st):
    bits = [0, 0, 0, 0, 0, 0, 0, 0] # 255/32 ~ 8 (32 bit ints for Java (this is not true for python))
    for s in st:
        idx = correct_idx(ord(s))
        bit = correct_bit(ord(s))
        if bits[idx] & (1 << bit): return False
        bits[idx] = bits[idx] | (1 << bit)
    return True

def correct_idx(ordinal_val):
    return ordinal_val/32

def correct_bit(ordinal_val):
    return ordinal_val % 32 

def all_unique_with_list_assume_ascii(st):
    seen = []
    for i in xrange(0, 255):
        seen.append(0)
    for s in st:
        if seen[ord(s)]:
            return False
        seen[ord(s)] = 1
    return True

# A messy one-liner
#
# Works by sorting the string, creating a new string by using `reduce` with 
# a function that concatenates the character only if it's not the same as 
# the last letter in the accumulated value (since in a sorted string, 
# duplicate characters will be together).
# Returns True if len(st) <= 1
# i.e., this is bad at everything
#
# O(n^2) time
def all_unique_one_liner(st):
    return len(reduce(lambda x,y : x if x[-1] == y else x + y, sorted(st))) == len(st) if len(st) > 1 else True

# A set-based solution that violates the secondary requirement
# O(n) time
def all_unique_with_set(st):
    seen = set()
    for c in st:
        if c in seen:
            return False
        seen.add(c)
    return True

# O(1) space, O(n^2) time
def all_unique_slow(st):
    for idx, c in enumerate(st):
        for x in xrange(idx): 
            if st[x] == c:
                return False
    return True

tests = ['', 'a', 'abcdefghijklmnopqrstuvwxyz', 'a_^*&!unique', 'notsounique:()']

for t in tests:
    print all_unique_with_set(t)
    print all_unique_slow(t)
    print all_unique_one_liner(t)
    print all_unique_with_list_assume_ascii(t)
    print all_unique_with_bit_vector_assume_ascii(t)
    print
