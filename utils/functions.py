#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.26.
@author: vik1228
"""
from itertools import product


def generate_numbers_with_builtin(n=2, nums='357'):
    """
    Generate numbers with builtin method/class (itertools.product)
    :param n: number of digits (n-wide)
    :param nums: possible digits
    :return: list of numbers (string-format)
    """
    products = [i for i in product(*([nums] * n))]
    return [''.join(number) for number in products]


def generate_numbers_with_brute_force(n=2, nums='357'):
    """
    Generate numbers with brute force
    :param n: number of digits (n-wide)
    :param nums: possible digits
    :return: list of numbers (string-format)
    """
    all_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    stop = '1' + '0' * n
    all_n_wide_numbers = ["{:0{}.{}f}".format(i, n, 0) for i in range(0, int(stop))]
    digits = {*nums}
    other_digits = all_digits.difference(digits)
    numbers = []
    for number in all_n_wide_numbers:
        for other_digit in other_digits:
            if other_digit in number:
                break
        else:
            numbers.append(number)
    return numbers


def generate_numbers_with_backtrack(n=2, nums='357'):
    """
    Generate numbers with backtrack
    :param n: number of digits (n-wide)
    :param nums: possible digits
    :return: list of numbers (string-format)
    """
    combinations = []

    def backtrack(combination):
        if len(combination) == n:
            combinations.append(''.join(combination))
            return
        for num in [*nums]:
            combination.append(num)
            backtrack(combination)
            combination.pop()

    backtrack([])
    return combinations
