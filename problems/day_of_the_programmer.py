# https://www.hackerrank.com/contests/w29/challenges/day-of-the-programmer

# !/bin/python3

import sys

y = int(input().strip())
# your code goes here

# first 8 months, feb will be calculated accordingly temporary 28
month_days = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31, 'jun': 30, 'jul': 31, 'aug': 31}

is_leap_y = False
is_transition = False

# Julian Calendar
if 1700 <= y <= 1917:
    is_leap_y = y % 4 == 0

# transition
if y == 1918:
    is_leap_y = y % 4 == 0
    is_transition = True

# Gregorian Calendar
if y > 1919:
    is_leap_y = (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0))

if is_leap_y:
    month_days['feb'] = 29

if is_transition:
    month_days['feb'] -= 14

days = 256 - sum(month_days.values())

print(str(days) + ".09" + "." + str(y))
