import random

def get_bingo_card():
    b = ['B' + str(n) for n in random.sample(range(1, 16), 5)]
    i = ['I' + str(n) for n in random.sample(range(16, 31), 5)]
    n = ['N' + str(n) for n in random.sample(range(31, 46), 4)]
    g = ['G' + str(n) for n in random.sample(range(46, 61), 5)]
    o = ['O' + str(n) for n in random.sample(range(61, 76), 5)]
    return b + i + n + g + o
