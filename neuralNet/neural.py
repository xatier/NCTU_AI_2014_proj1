#!/usr/bin/env pypy3

import math

# input raws
t = []
label = [0, 1]

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



def learning(t, label, w):

    k = i = 0
    learning_limit = 800
    # learning times
    while k < learning_limit:

        in_ = -sum( t[i][j] * w[j] for j in range(228) )

        g = 1 / (1.0 + math.e**in_)

        l = 0 if i < 400 else 1

        # learing progress
        if (label[l] == 0 and g <= 0.5) or \
           (label[l] == 1 and g > 0.5):
            pass
        else:
            # not correct
            k //= 2
            Err = label[l] - g;

            # adjust weight
            for j in range(228):
                w[j] += 0.05 * Err * g * (1-g) * t[i][j]

        k += 1
        i = (i+1) % 800



def test(t, label, w):
    """ run training data """

    k = 0;
    for i in range(800):
        in_ = 0.0
        for j in range(228):
            in_ -= t[i][j] * w[j];

        g = 1 / (1.0 + math.e**in_)

        l = 0 if i < 400 else 1

        if label[l] == 0 and g <= 0.5:
            k += 1
        elif label[l] == 1 and g > 0.5:
            k += 1


    print("{} correct".format(k))


run(t)
learning(t, label, w)
test(t, label, w)
