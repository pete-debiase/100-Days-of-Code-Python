#!/usr/bin/python
"""Randomization - virtual coin toss program"""

import random

random_integer = random.randint(0, 1)
print("Heads" if random_integer == 1 else "Tails")
