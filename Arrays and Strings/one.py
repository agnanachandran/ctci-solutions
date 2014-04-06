#
# 1.1
#
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
#

# A somewhat pythonic solution that violates the secondary requirement
def all_unique(st):
    pass # TODO

# A set-based solution that violates the secondary requirement
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
    print ''
