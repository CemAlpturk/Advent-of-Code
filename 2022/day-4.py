from typing import Tuple


def full_overlap(task1: Tuple[int, int], task2: Tuple[int, int]) -> bool:
    overlap1 = task1[0] <= task2[0] and task1[1] >= task2[1]
    overlap2 = task2[0] <= task1[0] and task2[1] >= task1[1]

    return overlap1 or overlap2


def not_overlap(task1: Tuple[int, int], task2: Tuple[int, int]) -> bool:
    return task1[1] < task2[0] or task2[1] < task1[0]

# Part 1


file = 'inputs/day-4.txt'

with open(file) as f:
    lines = f.readlines()

num = 0
for line in lines:
    vals = line.split('\n')[0]
    val1, val2 = vals.split(',')
    task1 = tuple(int(x) for x in val1.split('-'))
    task2 = tuple(int(x) for x in val2.split('-'))
    num += full_overlap(task1, task2)

print(num)

num = 0
for line in lines:
    vals = line.split('\n')[0]
    val1, val2 = vals.split(',')
    task1 = tuple(int(x) for x in val1.split('-'))
    task2 = tuple(int(x) for x in val2.split('-'))
    num += not_overlap(task1, task2)

print(1000 - num)
