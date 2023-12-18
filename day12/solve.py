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
    widhts: List[int]

    @classmethod
    def from_line(cls, line: str):
        springs, widhts = line.split(" ")
        widhts = [int(width) for width in widhts.split(",")]
        springs = [spring for spring in springs.split(".") if spring]
        return cls(
            springs=springs,
            widhts=widhts
        )

def solve_record(record: Record):
    max_width_index = max(range(len(record.widhts)), key=record.widhts.__getitem__)
    left_widths = record.widhts[:max_width_index]
    right_widths = record.widhts[max_width_index + 1:]
    current_width = record.widhts[max_width_index]
    x = 1 
    
def solve1(data: List[str]):
    records = [Record.from_line(line) for line in data]
    for record in records:
        solve_record(record)


def main():
    file_path = "day12/input.txt"

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