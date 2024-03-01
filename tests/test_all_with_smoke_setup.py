#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Created on 2024.02.29.
@author: vik1228
Simple (smoke) test for all generator
"""
from utils.functions import generate_numbers_with_builtin, generate_numbers_with_brute_force, generate_numbers_with_backtrack

N = 2
NUMS = '34'

EXPECTED_LENGTH = 4
EXPECTED_RESULT = {'33', '34', '43', '44'}

functions = [
    ("Generate with builtin", generate_numbers_with_builtin),
    ("Generate with brute force", generate_numbers_with_brute_force),
    ("Generate with backtrack", generate_numbers_with_backtrack)
]

for name, function in functions:
    numbers = function(N, NUMS)
    print(name, numbers)

    assert set(numbers) == EXPECTED_RESULT, (f"{name}: Generated numbers correct?! "
                                             f"{set(numbers)} vs {EXPECTED_RESULT}")

    assert len(numbers) == EXPECTED_LENGTH, (f"{name}: Number of generated numbers correct?! "
                                             f"{len(numbers)} vs {EXPECTED_LENGTH}")
