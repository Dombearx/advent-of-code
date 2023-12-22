from enum import Enum
from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit
from utils import read_data
import numpy as np
from tqdm import tqdm

def calc_hash(text):
    hash_value = 0
    for char in text:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value
def solve1(data: List[str]):
    input_array = data[0].strip()
    results = []
    for input_text in input_array.split(","):
        results.append(calc_hash(input_text))
    return sum(results)

@dataclass
class Lens:
    label: str
    focal_length: int

def solve2(data: List[str]):
    input_array = data[0].strip()
    boxes = [[] for _ in range(256)]
    for input_text in input_array.split(","):
        if "=" in input_text:
            label, focal_length = input_text.split("=")
            box_id = calc_hash(label)
            found_lenses = [i for i, lens in enumerate(boxes[box_id]) if lens.label == label]
            if found_lenses:
                lens_index = found_lenses[0]
                boxes[box_id][lens_index].focal_length = focal_length
            else:
                boxes[box_id].append(Lens(label=label, focal_length=focal_length))
        if "-" in input_text:
            label = input_text[:-1]
            box_id = calc_hash(label)
            found_lenses = [lens for lens in boxes[box_id] if lens.label == label]
            if found_lenses:
                boxes[box_id].remove(found_lenses[0])

    results = 0
    for box_index, box in enumerate(boxes):
        for index, lens in enumerate(box):
            results += (box_index + 1) * (index + 1) * int(lens.focal_length)
    return results

def main():
    data = read_data()
    # data = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]
    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")