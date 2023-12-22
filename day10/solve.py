from enum import Enum
from functools import reduce
from typing import List, Dict, Tuple
import re
from dataclasses import dataclass, field
import timeit
from memory_profiler import profile

from utils import read_file


class Direction(Enum):
    left = 0
    down = 1
    right = 2
    top = 3

PIPES = {
    (Direction.right, "7"): (Direction.down, Direction.right),
    (Direction.top, "7"): (Direction.left, Direction.left),
    (Direction.top, "|"): (Direction.top, None),
    (Direction.down, "|"): (Direction.down, None),
    (Direction.left, "F"): (Direction.down, Direction.left),
    (Direction.top, "F"): (Direction.right, Direction.right),
    (Direction.down, "J"): (Direction.left, Direction.right),
    (Direction.right, "J"): (Direction.top, Direction.left),
    (Direction.left, "L"): (Direction.top, Direction.right),
    (Direction.down, "L"): (Direction.right, Direction.left),
    (Direction.left, "-"): (Direction.left, None),
    (Direction.right, "-"): (Direction.right, None),
}


def get_animal_from_line(line: str):
    try:
        animal = line.index("S")
    except ValueError:
        return None
    return animal

@dataclass
class Position:
    x: int
    y: int

    def go_left(self):
        return Position(x=self.x - 1, y=self.y)
    def go_right(self):
        return Position(x=self.x + 1, y=self.y)
    def go_up(self):
        return Position(x=self.x, y=self.y - 1)
    def go_down(self):
        return Position(x=self.x, y=self.y + 1)
    def move(self, direction: Direction):
        if direction == Direction.left:
            return self.go_left()
        if direction == Direction.right:
            return self.go_right()
        if direction == Direction.down:
            return self.go_down()
        if direction == Direction.top:
            return self.go_up()

    def __hash__(self):
        return hash((self.x, self.y))

@dataclass
class Maze:
    maze: List[List[str]]
    relative_directions: Dict[Position, Direction] = field(default_factory=dict)

    def get_cell(self, position: Position):
        return self.maze[position.y][position.x]

    def mark_cell(self, position: Position):
        self.maze[position.y][position.x] = "M"

    def mark_horizontal(self, position: Position):
        self.maze[position.y][position.x] = "H"

    def print(self):
        for row in self.maze:
            print(" ".join(row))

def solve1(data: List[str]):
    maze_structure = []
    animal_pos = None
    for index, line in enumerate(data):
        animal = get_animal_from_line(line)
        if animal is not None:
            animal_pos = (animal, index)
        maze_structure.append(list(line))

    maze = Maze(maze=maze_structure)
    if animal_pos:
        print(animal_pos)
    next_pos = Position(x=animal_pos[0], y=animal_pos[1])

    next_pos = next_pos.go_left()
    previous_direction = Direction.left

    step_counter = 0
    while maze.get_cell(next_pos) != "S":
        cell = maze.get_cell(next_pos)
        previous_direction, _ = PIPES.get((previous_direction, cell), None)
        if previous_direction:
            next_pos = next_pos.move(previous_direction)
            step_counter += 1

    step_counter += 1

    return step_counter // 2

def solve2(data: List[str]):
    maze_structure = []
    animal_pos = None
    for index, line in enumerate(data):
        animal = get_animal_from_line(line)
        if animal is not None:
            animal_pos = (animal, index)
        maze_structure.append(list(line))

    maze = Maze(maze=maze_structure)
    if animal_pos:
        print(animal_pos)
    next_pos = Position(x=animal_pos[0], y=animal_pos[1])

    next_pos = next_pos.go_down()
    previous_direction = Direction.down

    loop_counter = 0
    while maze.get_cell(next_pos) != "S":
        cell = maze.get_cell(next_pos)
        if cell in "|LJ7F":
            maze.mark_horizontal(next_pos)
        else:
            maze.mark_cell(next_pos)
        previous_direction, relative_direction = PIPES.get((previous_direction, cell), None)
        maze.relative_directions[next_pos] = relative_direction
        if previous_direction:
            next_pos = next_pos.move(previous_direction)
    maze.mark_cell(next_pos)
    maze_width = len(maze.maze[0])

    for y, row in enumerate(maze.maze):
        directions = []
        number_of_pipes = 0
        if "H" not in row:
            continue
        for x, element in enumerate(row):
            if element == "H":
                number_of_pipes += 1
                directions.append(maze.relative_directions[Position(x=x, y=y)])

            elif element != "M":
                if number_of_pipes % 2 == 1 and len(directions) < 2:
                    row[x] = "I"
                elif number_of_pipes % 2 == 0 and len(directions) < 2:
                    continue
                elif number_of_pipes % 2 == 1 and directions[-1] != directions[-2]:
                    row[x] = "I"
                elif number_of_pipes % 2 == 0 and directions[-1] == directions[-2]:
                    row[x] = "I"

    maze.print()

    return 1

def main():
    file_path = "input.txt"

    data = read_file(file_path)
    data = [
        "..........",
        ".S------7.",
        ".|F----7|.",
        ".||....||.",
        ".||....||.",
        ".|L-7F-J|.",
        ".|..||..|.",
        ".L--JL--J.",
        "..........",
    ]
    # data = [
    #     "FF7FSF7F7F7F7F7F---7",
    #     "L|LJ||||||||||||F--J",
    #     "FL-7LJLJ||||||LJL-77",
    #     "F--JF--7||LJLJ7F7FJ-",
    #     "L---JF-JLJ.||-FJLJJ7",
    #     "|F|F-JF---7F7-L7L|7|",
    #     "|FFJF7L7F-JF7|JL---7",
    #     "7-L-JL7||F7|L7F-7F7|",
    #     "L.L7LFJ|||||FJL7||LJ",
    #     "L7JLJL-JLJLJL--JLJ.L",
    # ]
    print(solve2(data))


if __name__ == '__main__':
    elapsed_time = timeit.timeit(main, number=1)
    print(f"Elapsed time: {elapsed_time} seconds")
