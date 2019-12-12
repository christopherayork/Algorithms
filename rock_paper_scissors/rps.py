#!/usr/bin/python

import sys


def heaps_algorithm(a, n):
    if n == 1: return n
    for i in range(0, n - 1):
        heaps_algorithm(a, n - 1)
        if n % 2:
            a[n - 1], a[i] = a[i], a[n - 1]
        else:
            a[n - 1], a[0] = a[0], a[n - 1]
    heaps_algorithm(a, n - 1)


from itertools import permutations


def rock_paper_scissors(n):
    if n == 0: return [[]]
    rpm = ['rock', 'paper', 'scissors']
    # result = heaps_algorithm(rpm, n)
    perms = permutations(rpm, n)
    result = []
    for o in perms:
        print(o)
        result.append(list(o))
    print(result)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
