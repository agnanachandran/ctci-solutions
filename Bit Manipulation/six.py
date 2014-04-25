# 
# 5.6
# Write a program to swap odd and even bits in an integer with as few instructions as possible (e g , bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc)
#

def swap_bits(num):
    print bin(num)
    odds = num << 1
    evens = num >> 1
    odds &= 0xaaaaaaaa # 1010...1010
    evens &= 0x55555555
    print bin(odds | evens)

swap_bits(27)
