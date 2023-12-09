from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit
from functools import reduce

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def solve1(data: List[str]):
    times = re.findall("[0-9]+", data[0])
    distances = re.findall("[0-9]+", data[1])
    points = []
    for time, distance in zip(times, distances):
        time = int(time)
        distance = int(distance)
        for i in range(1, time - 1):
            my_distance = (time - i) * i
            if my_distance > distance:
                points.append((time + 1) - i * 2)
                break

    return reduce(lambda x, y: x*y, points)

def solve2(data: List[str]):
    data[0] = data[0].replace(" ", "")
    data[1] = data[1].replace(" ", "")
    times = re.findall("[0-9]+", data[0])
    distances = re.findall("[0-9]+", data[1])
    points = []
    for time, distance in zip(times, distances):
        time = int(time)
        distance = int(distance)
        for i in range(1, time - 1):
            my_distance = (time - i) * i
            if my_distance > distance:
                points.append((time + 1) - i * 2)
                break

    return points[0]
    

def main():
    file_path = "day6/input.txt"

    data = read_file(file_path)
    # data = [
    #     "Time:      7  15   30",
    #     "Distance:  9  40  200"
    # ]
    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")