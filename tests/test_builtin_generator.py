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
    print('List of numbers:')
    print(numbers)
    length_of_list = len(numbers)
    str_length_of_list = f'Length of list: {length_of_list}'
    print(str_length_of_list)
    expected_length = pow(len(nums), n)
    str_expected = f"(Expected length {len(nums)}^{n} = {expected_length})"
    print(str_expected)
    assert length_of_list == expected_length, "get what we expected ?!? [in length]"
    t_exe = end - start
    str_exe = f"Execution time: {t_exe} ns , {t_exe / 1000} us , {t_exe / 1000000} ms, {t_exe / 1000000000} s "
    print(str_exe)
    print('*' * 100)

    file_name = f"generate_with_builtin_{n}_{nums}.txt"
    with open(file_name, "w") as file:
        file.write(f"Generate with builtin (N={n}, nums={nums})")
        file.write('\n')
        file.write(str(numbers))
        file.write('\n')
        file.write(str_length_of_list)
        file.write('\n')
        file.write(str_expected)
        file.write('\n')
        file.write(str_exe)
