#!/usr/bin/env pypy3

import math

# input raws
t = []
label = [0, 1]

w = [1.0] * 228

def run():
    global t
    global label
    global w

    # read the file
    train_f = open("../TAdrop/train.txt", "r");

    for line in train_f:
        t += [ [ int(x) for x in line.split() ] ]

    train_f.close()


    # normalization make sum(t) == 1
    for i in range(800):
        s_t = sum(t[i])
        t[i] = [ t[i][x]/s_t for x in range(228) ]

    # learning
    k = i = 0
    while i < 800:
        in_ = 0.0
        for j in range(228):
            in_ -= t[i][j] * w[j]

        g = 1 / (1.0 + math.e**in_)

        # learing progress
        #if k < 800*800*10:
        if k < 800*100*10:
            k += 1
        else:
            break

        if label[i >= 400] == 0 and g <= 0.5:
            i = (i+1) % 800
            continue
        elif label[i >= 400] == 1 and g > 0.5:
            i = (i+1) % 800
            continue

        # not correct
        k -= 2
        Err = label[i >= 400] - g;

        # adjust weight
        for j in range(228):
            w[j] += 0.01 * Err * g * (1-g) * t[i][j]


        i = (i+1) % 800

    # run training data
    k = 0;
    for i in range(800):
        in_ = 0.0
        for j in range(228):
            in_ -= t[i][j] * w[j];

        g = 1 / (1.0 + math.e**in_)

        if label[i >= 400] == 0 and g <= 0.5:
            k += 1
        elif label[i >= 400] == 1 and g > 0.5:
            k += 1


    print("{} correct".format(k))

run()
