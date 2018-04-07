#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

T = input()
for t in xrange(T):
    A = input()
    win = False
    if A == 20:
        rows, cols = 4, 5
    else:
        rows, cols = 10, 20
    trees = [[False for x in xrange(cols)] for y in xrange(rows)]
    for y, row in enumerate(trees):
        if win:
            break
        for x, tree in enumerate(row):
            if win:
                break
            while tree is False:
                print max(2, min(rows - 1, y + 2)), max(2, min(cols - 1, x + 2))
                sys.stdout.flush()
                i, j = map(int, raw_input().split(' '))
                if i == -1 and j == -1:
                    sys.exit(-1)
                if i == 0 and j == 0:
                    win = True
                    break
                trees[i - 1][j - 1] = True
                tree = trees[y][x]
