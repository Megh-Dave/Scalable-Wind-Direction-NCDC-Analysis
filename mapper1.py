#!/usr/bin/env python

import re
import sys

def extract_year_month(date):
    return date[:6]

for line in sys.stdin:
    val = line.strip()
    (year_month, direction, q) = (val[15:21], val[60:63], val[63:64])
#(year, direction, q) = (val[15:21], val[60:63], val[63:64])
    if direction != "+999" and re.match("[01459]", q):
        #year_month = extract_year_month(year)
        print "%s\t%s" % (year_month, direction)
