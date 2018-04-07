#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit

T = int(raw_input())
for t in xrange(T):
    start_time = timeit.default_timer()
    raw_input()
    case = map(int, raw_input().split(' '))
    correct_sort = sorted(case)
    correct_sort_even, correct_sort_odd = [], []
    case_even, case_odd = [], []
    for i, x in enumerate(correct_sort):
        if i & 1:
            correct_sort_odd.append(x)
            case_odd.append(case[i])
        else:
            correct_sort_even.append(x)
            case_even.append(case[i])
    sorted_case_even = sorted(case_even)
    sorted_case_odd = sorted(case_odd)

    for i in xrange(len(case)):
        if i & 1 and sorted_case_odd[i / 2] != correct_sort_odd[i / 2]:
            print 'Case #{}: {}'.format(t + 1, i)
            break
        elif sorted_case_even[i / 2] != correct_sort_even[i / 2]:
            print 'Case #{}: {}'.format(t + 1, i)
            break
    else:
        print 'Case #{}: OK'.format(t + 1)
            
    print timeit.default_timer() - start_time
