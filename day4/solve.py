from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

def solve1(data: List[str]):
    points = 0
    for line in data:
        first_part, second_part = line.split("|")
        first_part = first_part.split(":")[-1]
        winning_numbers = re.findall("[0-9]+", first_part)
        my_numbers = re.findall("[0-9]+", second_part)
        power = sum(my_number in winning_numbers for my_number in my_numbers)
        if power:
            points += 2**(power-1)
    return points

def solve2(data: List[str]):
    points = 0
    cards_to_wins = []
    for line in data:
        first_part, second_part = line.split("|")
        first_part = first_part.split(":")[-1]
        winning_numbers = re.findall("[0-9]+", first_part)
        my_numbers = re.findall("[0-9]+", second_part)
        number_of_winning_numbers = sum(my_number in winning_numbers for my_number in my_numbers)
        cards_to_wins.append(number_of_winning_numbers)
    
    my_cards = list(range(len(data)))
    points = len(my_cards)
    while my_cards:
        my_new_cards = []
        for card in my_cards:
            my_new_cards += [card + x + 1 for x in range(cards_to_wins[card])]
            points += cards_to_wins[card]
        my_cards = my_new_cards

    return points


def main():
    file_path = "day4/input.txt"

    data = read_file(file_path)
    # data = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    # ]

    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")