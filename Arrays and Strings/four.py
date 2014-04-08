#
# 1.4
#
# Write a method to decide if 2 strings are anagrams or not.
#

def are_anagrams(s1, s2):
    if s1 is None or s2 is None or len(s1) != len(s2): return False 
    d1 = {}
    d2 = {}
    for i in xrange(len(s1)):
        freq1 = d1.get(s1[i], 0)
        d1[s1[i]] = freq1 + 1
        freq1 = d1.get(s1, 0)
        freq2 = d2.get(s2[i], 0)
        d2[s2[i]] = freq2 + 1
        freq2 = d2.get(s2, 0)
    return d1 == d2

print are_anagrams('abcde', 'edcba')
print are_anagrams('hello', 'hello')
print are_anagrams('', '')
print are_anagrams(None, None)
