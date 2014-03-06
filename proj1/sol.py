#!/usr/bin/env python3

import math
import copy

# input raws
c1 = []
c2 = []
c1_avg = []
c2_avg = []

def init():
    global c1
    global c2
    global c1_avg
    global c2_avg

    # read the file
    train_f = open("TAdrop/train.txt", "r");

    ct = 0
    for line in train_f:
        if ct < 400:
            c1 += [ [ int(x) for x in line.split() ] ]
        else:
            c2 += [ [ int(x) for x in line.split() ] ]

        ct += 1

    train_f.close()


    # normalization make sum(c1), sum(c2) == 1
    for i in range(400):
        s_c1 = sum(c1[i])
        s_c2 = sum(c2[i])
        c1[i] = [ c1[i][x]/s_c1 for x in range(228) ]
        c2[i] = [ c2[i][x]/s_c2 for x in range(228) ]

    # the average of frequency of each row
    for i in range(228):
        c1_avg.append( sum( c1[x][i] for x in range(400) ) / 400 )
        c2_avg.append( sum( c2[x][i] for x in range(400) ) / 400 )



def check(l):
    global c1_avg
    global c2_avg

    # we don't want to modify the input list
    # (python pass lists by ref in default)
    l_ = copy.deepcopy(l)

    # normalize it
    s_l = sum(l_)

    # in TA's stupid test cases, there's a 'no-freture' row ...
    if s_l == 0:
        return True

    l_ = [ l[i]/s_l for i in range(228) ]

    # the 'distance' in a 228-dimension space
    # distance = sqrt ( sum of (difference)^2 in each dimension )

    s1 = math.sqrt( sum( (c1_avg[i] - l_[i])**2 for i in range(228) ) )
    s2 = math.sqrt( sum( (c2_avg[i] - l_[i])**2 for i in range(228) ) )

    # return true if the distance from l to c1_avg is less
    if s1 < s2:
        return True
    else:
        return False

init()

# make a self-modify algorithm for 200 rounds
for _ in range(200):

    for i in range(400):
        if not check(c1[i]):         # fail: c1 -> c2
            for j in range(228):
                c1_avg[j] -= (c1_avg[j] - c1[i][j]) * 0.0001

        if check(c2[i]):             # fail: c2 -> c1
            for j in range(228):
                c2_avg[j] -= (c2_avg[j] - c2[i][j]) * 0.0001



"""
ct = 0
c1t = 0   # c1 -> c1
c1f = 0   # c1 -> c2
c2t = 0   # c2 -> c2
c2f = 0   # c2 -> c1

# read the file again
train_f = open("TAdrop/train.txt", "r");

for line in train_f:
    l = [ int(x) for x in line.split() ]

    if ct < 400:
        if check(l):
            c1t += 1
        else:
            c1f += 1
    else:
        if check(l):
            c2f += 1
        else:
            c2t += 1

    ct += 1

train_f.close()

print(c1t)
print(c1f)
print(c2f)
print(c2t)
"""

"""
383
17
16
384
"""

# read the test file
test_f = open("TAdrop/test.txt", "r");

for line in test_f:
    l = [ int(x) for x in line.split() ]

    if check(l):
        print("1")
    else:
        print("2")

test_f.close()
