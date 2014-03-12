#!/usr/bin/env pypy3

import math

# input raws
t = []

w = [0.5] * 228

def run(t):

    # read the file
    train_f = open("../TAdrop/train.txt", "r");

    for line in train_f:
        t += [ [ int(x) for x in line.split() ] ]

    train_f.close()


    # normalization make sum(t) == 1
    for i in range(800):
        s_t = sum(t[i])
        t[i] = [ t[i][x]/s_t for x in range(228) ]



def learning(t, w):

    k = i = 0
    learning_limit = 800
    # learning times
    while k < learning_limit:

        in_ = -sum( [ t[i][j] * w[j] for j in range(228) ] )

        g = 1 / (1.0 + math.e**in_)

        # label
        l = 0 if i < 400 else 1

        # learning progress
        if (l == 0 and g < 0.5) or \
           (l == 1 and g > 0.5):
            pass
        else:
            # not correct
            k //= 2

            # adjust weight
            adj = 0.05 * (l - g) * g * (1 - g)
            for j in range(228):
                w[j] += adj * t[i][j]

        k += 1
        i = (i+1) % 800


def check(l, w):
    in_ = -sum( [ l[j] * w[j] for j in range(228) ] )

    g = 1 / (1.0 + math.e**in_)

    if g < 0.5:
        return True
    else:
        return False


def test(t, w):
    """ run training data """

    k = 0;
    for i in range(800):
        in_ = 0.0
        for j in range(228):
            in_ -= t[i][j] * w[j];

        g = 1 / (1.0 + math.e**in_)

        l = 0 if i < 400 else 1

        if l == 0 and g < 0.5:
            k += 1
        elif l == 1 and g > 0.5:
            k += 1


    print("{} correct".format(k))


run(t)
learning(t, w)
test(t, w)


# testing
"""
ct = 0
c1t = 0   # c1 -> c1
c1f = 0   # c1 -> c2
c2t = 0   # c2 -> c2
c2f = 0   # c2 -> c1

# read the file again
train_f = open("../TAdrop/train.txt", "r");

for line in train_f:
    l = [ int(x) for x in line.split() ]

    if ct < 400:
        if check(l, w):
            c1t += 1
        else:
            c1f += 1
    else:
        if check(l, w):
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
387
13
0
400
"""

# read the test file
test_f = open("../TAdrop/test.txt", "r");

for line in test_f:
    l = [ int(x) for x in line.split() ]

    if check(l, w):
        print("1")
    else:
        print("2")

test_f.close()
