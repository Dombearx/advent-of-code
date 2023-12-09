import re
from typing import List

from utils import read_file


def solve1(data):
    filtered_lines = [re.sub("\D", "", line) for line in data]
    return sum(
        int("".join([digits[0], digits[-1]])) for digits in filtered_lines if digits
    )

def solve2(data):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    filtered_lines = []
    for line in data:
        digits_indexes = [(digit, pos) for pos, digit in enumerate(line) if digit.isdigit()]
        for index, word in enumerate(words):
            digits_indexes += [(str(index + 1), m.start()) for m in re.finditer(word, line)]

        digits_indexes = sorted(digits_indexes, key=lambda x: x[1])
        if digits_indexes:
            filtered_lines.append("".join([digits_indexes[0][0], digits_indexes[-1][0]]))

    return sum(
        int(number) for number in filtered_lines
    )

def solve_warmup(data: List[str]):
    return data[0].count("(") - data[0].count(")")

def solve_warmup2(data: List[str]):
    f = 0
    for index, char in enumerate(data[0]):
        if char == "(":
            f += 1
        if char == ")":
            f -= 1
        if f < 0:
            return index + 1

def main():
    file_path = "input.txt"
    data = read_file(file_path)
    print(solve1(data))
    print(solve2(data))

    warmup_data = read_file("input2.txt")
    print(solve_warmup(warmup_data))
    print(solve_warmup2(warmup_data))


if __name__ == '__main__':
    main()