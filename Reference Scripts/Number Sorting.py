#!~/.pyenv/versions/3.11.6/bin/python

# Copyright (c) 2024 Cutieguwu | Olivia Brooks
#
# -*- coding:utf-8 -*-
# @Title: Numerical bubble sorter.
# @Author: Cutieguwu | Olivia Brooks
# @Email: owen.brooks77@gmail.com | obroo2@ocdsb.ca
# @Description: Simple Least to Greatest bubble sorter.
#
# @Script: 1.py
# @Date Created: 20 Mar, 2024
# @Last Modified: 21 Mar, 2024
# @Last Modified by: Cutieguwu | Olivia Brooks

from os import path

with open(path.dirname(__file__) + "/sortfiles/sort1.txt", "rt") as f:
    sortData = f.readlines()

print(f"Fetched from ./sortfiles/sort1.txt\n{sortData}")
print("Cleaning up...")

for i in range(0, len(sortData)):
    sortData[i] = int("".join(c for c in sortData[i] if c.isdigit()))

def is_sorted():
    IS_SORTED = []
    for i in range(0, len(sortData) - 1):
        if sortData[i] > sortData[i + 1]:
            IS_SORTED.append(False)
        else:
            IS_SORTED.append(True)
    
    if False in IS_SORTED:
        IS_SORTED_FLAG = False
    else:
        IS_SORTED_FLAG = True
    return IS_SORTED_FLAG

while is_sorted() is False:
    for i in range(0, len(sortData) - 1):
        if sortData[i] > sortData[i + 1]:
            sortTemp = sortData[i + 1]
            sortData[i + 1] = sortData[i]
            sortData[i] = sortTemp

print("Finished.")
print(f"Cleaned data:\n{sortData}")