from functools import reduce
from typing import List
import re
from dataclasses import dataclass
import timeit

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()
    
def get_base_strength(hand):
    pass

def get_card_strength(card: str):
    if card.isnumeric:
        return int(card)
    figures = ["TJQKA"]
    return figures.index(card) + 10
    

def compare_hands(h1, h2):
    base_strength_1 = get_type_strength(h1)
    base_strength_2 = get_type_strength(h2)

    for c1, c2 in zip(h1, h2):
        if c1 > c2:
            pass
        if c2 > c1:
            pass

def solve1(data: List[str]):
    hands = [line.split() for line in data]
    hands = sorted(hands, key=compare_hands)

def main():
    file_path = "day7/input.txt"

    data = read_file(file_path)
    data = [
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483"
    ]
    print(solve1(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)

    print(f"Elapsed time: {elapsed_time} seconds")