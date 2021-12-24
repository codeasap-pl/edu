#!/usr/bin/env python

# Find the sum of all the multiples of 3 or 5 below 1000.

print(sum([_  for _ in range(1000) if _ % 3 == 0 or _ % 5 == 0]))
