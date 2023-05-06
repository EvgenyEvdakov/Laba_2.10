#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sum_modulo(*args):
    if args:
        zero = 0
        zero_index = args.index(zero)
        return sum(args[zero_index+1:])


if __name__ == "__main__":
    print(sum_modulo(1, 2, 3, 0, 4, -5, 6))
    print(sum_modulo(0, 5, -7, 9, -2))
    print(sum_modulo(-2, 7, 0, 3, -8, -5, 0, 1))
    print(sum_modulo())