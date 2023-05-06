#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def product_args_before_min(*args):
    if args:
        # Принимает минимальное значения среди всех аргументов
        min_value = min(args)
        # Принимает индекс минимального значения среди всех аргументов
        min_index = args.index(min_value)
        return min_index * sum(args[:min_index])
    return None


if __name__ == "__main__":
    print(product_args_before_min(1, 2, 3, 4, 5, 6, 7))
    print(product_args_before_min(11, 7, 13, 4, 2, 3))
    print(product_args_before_min())