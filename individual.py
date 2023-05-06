#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sum_modulo(*args):
    if not args:
        return None

    zero_found = False
    result = 0

    for arg in args:
        if zero_found:
            result += abs(arg)
        elif arg == 0:
            zero_found = True

    return result


if __name__ == "__main__":
    print(sum_modulo(1, 2, 3, 0, 2, 6))
    print(sum_modulo(-1, -2, -3))
    print(sum_modulo())