#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.26.
@author: vik1228
Number generator 
"""
from itertools import product
import time


def generate_numbers_with_builtin(n=5, nums='357'):
    """
    Generate numbers with builtin method/class (itertools.product)
    :param n: number of digits
    :param nums: possible numbers
    :return: list of numbers (string-format)
    """
    products = [i for i in product(*([nums] * n))]
    return [''.join(number) for number in products]


def generate_numbers_brute_force(n=2, nums='357'):
    all_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    stop = '1' + '0' * n
    all_n_wide_nums = ["{:0{}.{}f}".format(i, n, 0) for i in range(0, int(stop))]
    # print(all_n_wide_nums)
    digits = {*nums}
    other_digits = all_digits.difference(digits)
    numbers = []
    for num in all_n_wide_nums:
        for digit in other_digits:
            if digit in num:
                break
        else:
            numbers.append(num)
    return numbers


if __name__ == "__main__":
    n = 5
    nums = '357'

    print("Generate with builtin")
    start = time.time_ns()
    numbers = generate_numbers_with_builtin(n, nums)
    end = time.time_ns()
    print('List of numbers:')
    print(numbers)
    print(f'Length of list: {len(numbers)}')
    print(f"(Expected length {len(nums)}^{n} = {pow(len(nums),n)})")
    t_exe = end-start
    print(f"Execution time: {t_exe} ns , {t_exe/1000} us , {t_exe/1000000} ms, {t_exe/1000000000} s ")
    print('*' * 100)

    print("Generate with brute force")
    start = time.time_ns()
    numbers = (generate_numbers_brute_force(n, nums))
    end = time.time_ns()
    print('List of numbers:')
    print(numbers)
    print(f'Length of list: {len(numbers)}')
    print(f"(Expected length {len(nums)}^{n} = {pow(len(nums),n)})")
    t_exe = end-start
    print(f"Execution time: {t_exe} ns , {t_exe/1000} us , {t_exe/1000000} ms, {t_exe/1000000000} s ")
    print('*' * 100)
