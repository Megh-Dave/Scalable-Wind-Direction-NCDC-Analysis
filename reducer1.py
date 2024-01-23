#!/usr/bin/env python

import sys

(last_key, sum_direction, directions_list) = (None, 0, [])

for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    direction = int(val)

    if last_key and last_key != key:
        average_direction = sum_direction / len(directions_list)
        print "%s\t%s" % (last_key, average_direction)
        (last_key, sum_direction, directions_list) = (key, direction, [direction])
    else:
        (last_key, sum_direction, directions_list) = (key, sum_direction + direction, directions_list + [direction])

if last_key:
    average_direction = sum_direction / len(directions_list)
    print "%s\t%s" % (last_key, average_direction)
