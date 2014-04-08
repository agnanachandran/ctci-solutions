#
# 1.5
#
# Write a method to replace all spaces in a string with '%20'

def url_encode(st):
    return st.replace(' ', '%20')

def url_encode_no_cheating(st):
    new = ''
    for s in st:
        if s == ' ':
            new += '%20'
        else:
            new += s
    return new

tests = ['hello!', 'hello! ', '  hello! ','   ']
for test in tests:
    print url_encode(test)
    print url_encode_no_cheating(test)
