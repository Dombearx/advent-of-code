from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit
from memory_profiler import profile

from utils import read_file

@dataclass
class Map:
    from_number: int
    to_number: int
    change: int

@dataclass
class Range:
    start: int
    end: int

def find_corresponding(target, assignments: List[Map]):
    for assignment in assignments:
        if assignment.from_number <= target <= assignment.to_number:
            return target + assignment.change
    return target

def find_corresponding_ranges(range: Range, assignments: List[Map]) -> List[Range]:
    assignments = sorted(assignments, key=lambda x: x.from_number)
    next_ranges = []
    current_index_start = range.start
    for assignment in assignments:
        if current_index_start > assignment.to_number:
            continue
        if current_index_start < assignment.from_number:
            # no change
            next_ranges.append(Range(
                start=current_index_start,
                end=min(assignment.from_number - 1, range.end)
            ))
            if range.end < assignment.from_number:
                return next_ranges

            current_index_start = assignment.from_number

        next_ranges.append(Range(
            start=current_index_start + assignment.change,
            end=min(range.end, assignment.to_number) + assignment.change
        ))

        if range.end <= assignment.to_number:
            return next_ranges

        current_index_start = assignment.to_number + 1

    if range.end > assignments[-1].to_number:
        next_ranges.append(Range(
            start=current_index_start,
            end=range.end
        ))

    return next_ranges

def solve1(data: List[str]):
    to_find = "\n"
    targets = [int(seed) for seed in data[0].split(" ")[1:]]
    print(targets)

    current_index = 1

    while current_index < len(data):
        first_empty = data[current_index:].index(to_find)
        try:
            last_empty = data[current_index+1:].index(to_find)
        except ValueError:
            last_empty = len(data) - 1
        map_datas = data[current_index+first_empty+2:current_index+last_empty+1]
        print(map_datas)
        assignments = []
        for map_data in map_datas:
            to_val, from_val, range_val = [int(v) for v in map_data.split(" ")]
            assignments.append(Map(
                from_number=from_val,
                to_number=from_val + range_val,
                change=to_val - from_val
            ))
        targets = [find_corresponding(target, assignments) for target in targets]
        print(f"{targets=}")

        current_index += last_empty + 1
        print(f"{(current_index / len(data)) * 100}%")

    return min(targets)

def solve2(data: List[str]):
    to_find = "\n"
    real_targets = []
    targets = [int(seed) for seed in data[0].split(" ")[1:]]
    for t_start, t_range in zip(targets[::2], targets[1::2]):
        # print(t_start, t_range)
        real_targets.append(Range(
            start=t_start,
            end=t_start+t_range
        ))
    # print(targets)
    # print(real_targets)
    targets = real_targets

    current_index = 1

    while current_index < len(data):
        first_empty = data[current_index:].index(to_find)
        try:
            last_empty = data[current_index+1:].index(to_find)
        except ValueError:
            last_empty = len(data) - 1
        map_datas = data[current_index+first_empty+2:current_index+last_empty+1]
        # print(map_datas)
        assignments = []
        for map_data in map_datas:
            to_val, from_val, range_val = [int(v) for v in map_data.split(" ")]
            assignments.append(Map(
                from_number=from_val,
                to_number=(from_val + range_val) - 1,
                change=to_val - from_val
            ))
        targets = [item for target in targets for item in find_corresponding_ranges(target, assignments)]
        # print(f"{targets=}")

        current_index += last_empty + 1
        # print(f"{(current_index / len(data)) * 100}%")

    return min(t.start for t in targets)

@profile
def main():
    file_path = "input.txt"

    data = read_file(file_path)
    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")