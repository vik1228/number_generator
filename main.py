#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.26.
@author: vik1228
Number generator 
"""
import time
from utils.functions import generate_numbers_with_builtin, generate_numbers_brute_force, generate_numbers_with_backtrack


if __name__ == "__main__":
    # modify these parameters
    n = 5
    nums = '357'
    # Note: Brute force generator can cause MemoryError !

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

    print("Generate with backtrack")
    start = time.time_ns()
    numbers = generate_numbers_with_backtrack(n, nums)
    end = time.time_ns()
    print('List of numbers:')
    print(numbers)
    print(f'Length of list: {len(numbers)}')
    print(f"(Expected length {len(nums)}^{n} = {pow(len(nums),n)})")
    t_exe = end-start
    print(f"Execution time: {t_exe} ns , {t_exe/1000} us , {t_exe/1000000} ms, {t_exe/1000000000} s ")
    print('*' * 100)

