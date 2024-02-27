#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.26.
@author: vik1228
Basic tests for brute force generator
"""
from utils.functions import generate_numbers_brute_force
import time

print("Test cases for 'Generate with brute force'")

test_cases = [
    (1, '1234'),
    (2, '821'),
    (3, '46'),
    (5, '753'),
    (7, '02468')     # higher numbers cause MemoryError
]

for n, nums in test_cases:

    start = time.time_ns()
    numbers = generate_numbers_brute_force(n, nums)
    end = time.time_ns()
    print('List of numbers:')
    print(numbers)
    print(f'Length of list: {len(numbers)}')
    print(f"(Expected length {len(nums)}^{n} = {pow(len(nums), n)})")
    assert len(numbers) == pow(len(nums), n), "get what we expected ?!? [in length]"
    t_exe = end - start
    print(f"Execution time: {t_exe} ns , {t_exe / 1000} us , {t_exe / 1000000} ms, {t_exe / 1000000000} s ")
    print('*' * 100)
