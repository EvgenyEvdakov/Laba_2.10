#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sum_args_after_min(*args):
    if args:
        # Находим минимальное значение среди всех аргументов
        min_value = min(args)
        # Находим индекс минимального значения среди всех аргументов
        min_index = args.index(min_value)
        # Суммируем все аргументы, расположенные после индекса минимального значения
        return sum(args[min_index+1:])
    return None


if __name__ == "__main__":
    print(sum_args_after_min(1, 2, 3, 4, 5, 6, 7))
    print(sum_args_after_min(11, 7, 13, 4, 2, 3))
    print(sum_args_after_min())

