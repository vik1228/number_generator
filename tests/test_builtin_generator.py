#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.26.
@author: vik1228
Basic tests for builtin generator
"""
from utils.functions import generate_numbers_with_builtin
import time

print("Test cases for 'Generate with builtin'")

test_cases = [
    (1, '2468'),
    (2, '128'),
    (3, '64'),
    (5, '357'),
    (6, '13579')
]

for n, nums in test_cases:

    start = time.time_ns()
    numbers = generate_numbers_with_builtin(n, nums)
    end = time.time_ns()
    # print('List of numbers:')
    # print(numbers)
    print(f'Length of list: {len(numbers)}')
    print(f"(Expected length {len(nums)}^{n} = {pow(len(nums), n)})")
    assert len(numbers) == pow(len(nums), n), "get what we expected ?!? [in length]"
    t_exe = end - start
    print(f"Execution time: {t_exe} ns , {t_exe / 1000} us , {t_exe / 1000000} ms, {t_exe / 1000000000} s ")
    print('*' * 100)
