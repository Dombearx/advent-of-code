from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def solve1(data: List[str]):
    instructions = data[0].strip()
    elements = {}
    next_key = "AAA"
    for line in data[2:]:
        key, left, right = re.findall("[A-Z0-9]+", line)
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

    return step_number

def solve2(data: List[str]):
    instructions = data[0].strip()
    elements = {}
    
    for line in data[2:]:
        key, left, right = re.findall("[A-Z0-9]+", line)
        elements[key] = (left, right)

    next_keys = [key for key in elements.keys() if key[-1] == "A"]

    step_number = 0
    while any(key[-1] != "Z" for key in next_keys):
        step = instructions[step_number % len(instructions)]
        if step == "L":
            next_keys = [elements[key][0] for key in next_keys]
            step_number += 1
        if step == "R":
            next_keys = [elements[key][1] for key in next_keys]
            step_number += 1
        if any(key[-1] == "Z" for key in next_keys):
            # print(next_keys)
            pass
    return step_number

def main():
    file_path = "day8/input.txt"

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
    # data = [
    #     "LR",
    #     "",
    #     "11A = (11B, XXX)",
    #     "11B = (XXX, 11Z)",
    #     "11Z = (11B, XXX)",
    #     "22A = (22B, XXX)",
    #     "22B = (22C, 22C)",
    #     "22C = (22Z, 22Z)",
    #     "22Z = (22B, 22B)",
    #     "XXX = (XXX, XXX)",
    # ]
    # print(solve1(data))
    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")