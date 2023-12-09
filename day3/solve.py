from functools import reduce
from typing import List
import re

from utils import read_file


def solve1(data: List[str]):
    parts_sum = 0
    for index, line in enumerate(data):
        numbers = re.finditer("(\d+)", line)
        for match in numbers:
            chars_around = ""
            left, right = match.span()
            if left - 1 >= 0:
                left -= 1

            if right >= len(line):
                right -= 1

            chars_around += line[left] if left >= 0 else ""
            chars_around += line[right] if right < len(line) else ""

            chars_around += data[index - 1][left:right+1] if index - 1 >= 0 else ""
            chars_around += data[index + 1][left:right+1] if index + 1 < len(data) else ""
            chars_around = re.sub("[\d\.\n]", "", chars_around)
            if chars_around:
                parts_sum += int(match[0])

    return parts_sum

def solve2(data: List[str]):
    ratios_sum = 0
    for index, line in enumerate(data):
        gears = re.finditer("(\*)", line)
        for match in gears:
            numbers_same = re.finditer("(\d+)", line)
            numbers_above = re.finditer("(\d+)", data[index - 1]) if index - 1 >= 0 else []
            numbers_below = re.finditer("(\d+)", data[index + 1]) if index + 1 < len(data) else []
            numbers_around = []
            left, right = match.span()
            for number in numbers_same:
                number_left, number_right = number.span()
                if number_left == right or number_right == left:
                    numbers_around.append(int(number[0]))
            for number in numbers_above:
                number_left, number_right = number.span()
                if number_left <= left + 1 and left <= number_right:
                    numbers_around.append(int(number[0]))
            for number in numbers_below:
                number_left, number_right = number.span()
                if number_left <= left + 1 and left <= number_right:
                    numbers_around.append(int(number[0]))

            if len(numbers_around) == 2:
                ratios_sum += numbers_around[0] * numbers_around[1]

    return ratios_sum


def main():
    file_path = "input.txt"

    data = read_file(file_path)
    # data = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "..1..1#...",
    #     "617**9.....",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598.."
    # ]
    print(solve1(data))
    print(solve2(data))


if __name__ == '__main__':
    main()