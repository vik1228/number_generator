#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.26.
@author: vik1228
"""
from itertools import product


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
    """
    Generate numbers with brute force
    :param n: number of digits
    :param nums: possible numbers
    :return: list of numbers (string-format)
    """
    all_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    stop = '1' + '0' * n
    all_n_wide_nums = ["{:0{}.{}f}".format(i, n, 0) for i in range(0, int(stop))]
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


def generate_numbers_with_backtrack(n, nums):
    """
    Generate numbers with backtrack
    :param n: number of digits
    :param nums: possible numbers
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
