#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from itertools import izip

def isclose(a, b, rel_tol=1e-09, abs_tol=1e-09):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def rotate_in_plane(p, theta):
    x, y = p
    sin = math.sin(theta)
    cos = math.cos(theta)
    return x * cos - y * sin, y * cos + x * sin

def rotate_around_axis(axis, p, theta):
    if axis == 'x':
        rotated = rotate_in_plane((p[1], p[2]), theta)
        return p[0], rotated[0], rotated[1]
    elif axis == 'y':
        rotated = rotate_in_plane((p[2], p[0]), theta)
        return rotated[1], p[1], rotated[0]
    else:
        rotated = rotate_in_plane((p[0], p[1]), theta)
        return rotated[0], rotated[1], p[2]

def dist(a, b):
    return math.sqrt(sum((i - j) ** 2 for i, j in izip(a, b)))

def triangle_area(a, b, c):
    s = float(a + b + c) / 2.0
    try:
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    except:
        return 0

def projected_point(p):
    return p[0], p[2]

def rotate_cube(axis, cube, theta):
    return tuple(rotate_around_axis(axis, p, theta) for p in cube)

def projected_area(cube):
    """assume rotation around z-axis within 0 to PI / 4 and rotation around x-axis within PI / 4"""
    p0 = projected_point(cube[0])
    p1 = projected_point(cube[1])
    p2 = projected_point(cube[2])
    p5 = projected_point(cube[5])
    p6 = projected_point(cube[6])
    p7 = projected_point(cube[7])
    d01 = dist(p0, p1)
    d05 = dist(p0, p5)
    d15 = dist(p1, p5)
    d25 = dist(p2, p5)
    d02 = dist(p0, p2)
    d27 = dist(p2, p7)
    d57 = dist(p5, p7)
    d26 = dist(p2, p6)
    d67 = dist(p6, p7)
    return triangle_area(d02, d05, d25) + triangle_area(d25, d27, d57) + triangle_area(d01, d05, d15) + triangle_area(d27, d26, d67)

def mid_point_of_plane(*points):
    return tuple(sum(xs) / len(xs) for xs in izip(*points))

# see my draft for the position of each point
cube = (
    (-0.5, +0.5, +0.5),
    (+0.5, +0.5, +0.5),
    (-0.5, +0.5, -0.5),
    (+0.5, +0.5, -0.5),
    (-0.5, -0.5, +0.5),
    (+0.5, -0.5, +0.5),
    (-0.5, -0.5, -0.5),
    (+0.5, -0.5, -0.5),
)

rotated_pi_4 = rotate_cube('z', cube, math.pi / 4)
breakpoint = projected_area(rotated_pi_4)
T = input()
for t in xrange(T):
    A = input()
    if A < breakpoint:
        rotated_z_cube = cube
        left, right = 0, math.pi / 4
    else:
        rotated_z_cube = rotated_pi_4
        left, right = 0, 0.615516540655
    x_deg = (left + right) / 2.0
    rotated_cube = rotate_cube('x', rotated_z_cube, x_deg)
    area = projected_area(rotated_cube)
    while abs(A - area) >= 0.000001:
        if area > A:
            right = x_deg
        else:
            left = x_deg
        x_deg = (left + right) / 2.0
        rotated_cube = rotate_cube('x', rotated_z_cube, x_deg)
        area = projected_area(rotated_cube)
    p1 = mid_point_of_plane(rotated_cube[0], rotated_cube[1], rotated_cube[2], rotated_cube[3])
    p2 = mid_point_of_plane(rotated_cube[2], rotated_cube[3], rotated_cube[6], rotated_cube[7])
    p3 = mid_point_of_plane(rotated_cube[1], rotated_cube[3], rotated_cube[5], rotated_cube[7])
    print 'Case #{}:'.format(t + 1)
    print p1[0], p1[1], p1[2]
    print p2[0], p2[1], p2[2]
    print p3[0], p3[1], p3[2]
