#
# 1.8
#
# Assume you have a method isSubstring which checks if one word is a substring of another Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , "waterbottle" is a rotation of "erbottlewat")

def is_rotation(s1, s2):
    return s1 in s2+s2

test1 = ['erbottlewat', 'hello', 'joe']
test2 = ['waterbottle', 'elloh', 'oje']

for i in xrange(len(test1)):
    print is_rotation(test1[i], test2[i])
