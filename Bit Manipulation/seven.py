#
# 5.7
#

def log_two(num):
    power = 0
    while num != 1:
        num /= 2
        power += 1
    #print power
    return power


def findMissingInt(arr):
    #if not arr: return
    #N = len(arr) + 1
    #power = log_two(N)
    #twoPower = 2 ** power
    #diff = N - twoPower
    ## Can optimize by keeping track of which numbers are already good
    #freq = 0
    #for i in arr:
        #if ((1 << power) & i) > 0:
            ## matches
            #freq += 1
    #if freq == diff:
        ## correct # of numbers above twoPower
        ## Thus, there should now be an even number of numbers for any bit (could I apply this to the whole problem to start with; except for the last one?
        #freqs = [0 for x in range(power)]
        #for i in arr:
            #for j in range(0, power):
                #if ((1 << j) & i) > 0 and i <= twoPower:
                    #freqs[j] += 1
        #print freqs
        #num = 0
        #for i,val in enumerate(freqs):
            #if val % 2 != 0:
                #num += 2 ** i
                ## uneven
        #print num

        #power -= 1
    #else:

    #power += 1
    #print power
    #freqs = [0 for x in range(power)]
    #freqs1 = [0 for x in range(power)]
    #for i in arr:
        #for j in range(0, power):
            #if ((1 << j) & i) > 0:
                #freqs1[j] += 1
            #else:
                #freqs[j] += 1
    #print freqs
    #print freqs1
    #num = 0
    #for i,val in enumerate(freqs1):
        #if freqs1[i] != freqs[i]:
            #num += 2 ** i
            ## uneven
    #print num

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



def get_bit(i, j):
    return ((1 << j) & i) > 0

findMissingInt([5, 1, 4, 3, 0])
# 101 001 100 011 000
# 010
