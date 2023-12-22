from enum import Enum
from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit
from utils import read_data
import numpy as np
from tqdm import tqdm

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class Platform:
    def __init__(self, data):
        self.platform = np.array([list(line.strip()) for line in data])
        self.width = self.platform.shape[1]
        self.height = self.platform.shape[0]
        self.saved_states = {}

    def get_column(self, column_index) -> str:
        return "".join(self.platform[:, column_index])

    def get_row(self, row_index) -> str:
        return "".join(self.platform[row_index])

    def set_column(self, column_index, column_value):
        self.platform[:, column_index] = list(column_value)

    def set_row(self, row_index, row_value):
        self.platform[row_index] = list(row_value)

    def _tilt(self, max_range, get_line_func, set_line_func, parse_output_func):
        for line_index in range(max_range):
            line_string = parse_output_func(get_line_func(line_index))
            parts = line_string.split("#")
            new_parts = []
            for part in parts:
                rocks_count = sum(1 for element in part if element == "O")
                empty = "." * (len(part) - rocks_count)
                rocks = "O" * rocks_count
                new_parts.append(empty + rocks)
            new_line_string = parse_output_func("#".join(new_parts))
            set_line_func(line_index, new_line_string)

    def tilt(self, direction: Direction):
        if direction == Direction.NORTH:
            self._tilt(self.width, self.get_column, self.set_column, lambda x: "".join(reversed(x)))
        if direction == Direction.SOUTH:
            self._tilt(self.width, self.get_column, self.set_column, lambda x: x)
        if direction == Direction.WEST:
            self._tilt(self.height, self.get_row, self.set_row, lambda x: "".join(reversed(x)))
        if direction == Direction.EAST:
            self._tilt(self.height, self.get_row, self.set_row, lambda x: x)

    def count_load(self):
        rocks_per_row = np.count_nonzero(self.platform == "O", axis=1)
        return (rocks_per_row[::-1] * (np.arange(len(rocks_per_row)) + 1)).sum()

    def save_platform(self, iteration):
        byte_representation = self.platform.tobytes()
        if byte_representation in self.saved_states:
            return iteration - self.saved_states[byte_representation]
        self.saved_states[byte_representation] = iteration
        return False
def solve1(data: List[str]):
    platform = Platform(data=data)
    cycle = (Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST)
    number_of_cycles = 1_000_000_000
    for i in tqdm(range(number_of_cycles)):
        for direction in cycle:
            platform.tilt(direction)
        cycle_found = platform.save_platform(i)
        if cycle_found:
            print(f"{cycle_found = }")
            cycles_left = number_of_cycles - i - 1
            cycles_to_do = cycles_left % cycle_found
            for ii in range(cycles_to_do):
                for direction in cycle:
                    platform.tilt(direction)
            break

    print(f"load = {platform.count_load()}")


def main():
    data = read_data()
    # data = [
    #     "O....#....",
    #     "O.OO#....#",
    #     ".....##...",
    #     "OO.#O....O",
    #     ".O.....O#.",
    #     "O.#..O.#.#",
    #     "..O..#O..O",
    #     ".......O..",
    #     "#....###..",
    #     "#OO..#...."
    # ]
    print(solve1(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")