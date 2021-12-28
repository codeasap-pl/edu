#!/usr/bin/env python


def fib_rec(n):
    # F(n) = F(n-1) + F(n-2)
    if n > 1:
        return fib_rec(n - 1) + fib_rec(n - 2)
    return n


print(sum(list(filter(lambda n: n % 2 == 0, [fib_rec(i) for i in range(35)]))))
