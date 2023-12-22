from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

@dataclass
class Record:
    springs: List[str]
    widths: List[int]

    @classmethod
    def from_line(cls, line: str):
        springs, widths = line.split(" ")
        widths = [int(width) for width in widths.split(",")]
        springs = [spring for spring in springs.split(".") if spring]
        return cls(
            springs=springs,
            widths=widths
        )

def fit_width_in_springs(record: Record, width: int):
    solves = []
    for index, spring in enumerate(record.springs):
        if len(spring) < width:
            continue
        


    return solves

def solve_record(record: Record):
    max_width_index = max(range(len(record.widths)), key=record.widths.__getitem__)
    left_widths = record.widths[:max_width_index]
    right_widths = record.widths[max_width_index + 1:]
    current_width = record.widths[max_width_index]
    x = 1 
    
def solve1(data: List[str]):
    records = [Record.from_line(line) for line in data]
    return sum(solve_record(record) for record in records)


def main():
    file_path = "input.txt"

    data = read_file(file_path)
    data = [
        "???.### 1,1,3",
        ".??..??...?##. 1,1,3",
        "?#?#?#?#?#?#?#? 1,3,1,6",
        "????.#...#... 4,1,1",
        "????.######..#####. 1,6,5",
        "?###???????? 3,2,1"
    ]
    print(solve1(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")