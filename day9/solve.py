from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit
from memory_profiler import profile

from utils import read_file

def solve1(data: List[str]):
    new_values = []
    for line in data:
        last_elements = []
        new_line = [int(x) for x in line.split()]
        while any(item != 0 for item in new_line):
            last_elements.append(new_line[-1])
            new_line = [b - a for a, b in zip(new_line[:-1], new_line[1:])]
        new_values.append(sum(last_elements))
        print(sum(last_elements))
    return sum(new_values)

def solve2(data: List[str]):
    new_values = []
    for line in data:
        first_items = []
        new_line = [int(x) for x in line.split()]
        while any(item != 0 for item in new_line):
            first_items.append(new_line[0])
            new_line = [b - a for a, b in zip(new_line[:-1], new_line[1:])]
        difference = 0
        for val in reversed(first_items):
            difference = val - difference
        new_values.append(difference)
    return sum(new_values)


def main():
    file_path = "input.txt"

    data = read_file(file_path)
    # data = [
    #     "10 13 16 21 30 45",
    # ]
    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")