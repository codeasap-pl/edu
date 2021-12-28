#!/usr/bin/env python
import sys


def fibonacci_gen(limit):
    prev = 0
    curr = 1
    item = 0
    while item <= limit:
        item = prev + curr
        yield item
        prev = curr
        curr = item


limit = int(sys.argv[1] if len(sys.argv) > 1 else (4 * 10 ** 6))
print(sum([_ for _ in fibonacci_gen(limit) if _ % 2 == 0]))
