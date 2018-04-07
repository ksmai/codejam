#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def read_input():
    T = int(raw_input())
    return map(
        lambda t: (int(t[0]), t[1]),
        [raw_input().split(' ') for i in xrange(T)],
    )

def solve(d, p):
    strength = 1
    damage = 0
    node = [strength, 0]
    shoots = []
    for command in p:
        if command == 'C':
            shoots.append(node)
            damage += node[0] * node[1]
            strength *= 2
            node = [strength, 0]
        else:
            node[1] += 1
    shoots.append(node)
    damage += node[0] * node[1]

    n = 0
    while damage > d:
        node = shoots[-1]
        if not node or node[0] == 1:
            return -1
        if node[1] > 0:
            new_damage = damage - node[0] * node[1] / 2
            if new_damage > d:
                shoots.pop()
                shoots[-1][1] += node[1]
                damage = new_damage
                n += node[1]
            else:
                return n + int(math.ceil(float(damage - d) * 2 / node[0]))
        else:
            shoots.pop()

    return n


import timeit
cases = read_input()
for i, case in enumerate(cases):
    start_time = timeit.default_timer()
    ans = solve(*case)
    elapsed = timeit.default_timer() - start_time
    if ans == -1:
        print 'Case #{}: IMPOSSIBLE'.format(i + 1)
    else:
        print 'Case #{}: {}'.format(i + 1, ans)
    print elapsed
