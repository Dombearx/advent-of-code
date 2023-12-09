from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit
from memory_profiler import profile

from utils import read_file

def solve1(data: List[str]):
    instructions = data[0]
    elements = {}
    next_key = "AAA"
    for line in data[2:]:
        key, left, right = re.findall("[A-Z]+", line)
        elements[key] = (left, right)

    step_number = 0
    while next_key != "ZZZ":
        step = instructions[step_number % len(instructions)]
        if step == "L":
            next_key = elements[next_key][0]
            step_number += 1
        if step == "R":
            next_key = elements[next_key][1]
            step_number += 1
        print(next_key)
        if next_key == "MLV":
            x = 1
    return step_number


def main():
    file_path = "input.txt"

    data = read_file(file_path)
    # data = [
    #     "RL",
    #     "\n",
    #     "AAA = (BBB, CCC)",
    #     "BBB = (DDD, EEE)",
    #     "CCC = (ZZZ, GGG)",
    #     "DDD = (DDD, DDD)",
    #     "EEE = (EEE, EEE)",
    #     "GGG = (GGG, GGG)",
    #     "ZZZ = (ZZZ, ZZZ)"
    # ]
    # data = [
    #     "LLR",
    #     "",
    #     "AAA = (BBB, BBB)",
    #     "BBB = (AAA, ZZZ)",
    #     "ZZZ = (ZZZ, ZZZ)"
    # ]
    print(solve1(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")