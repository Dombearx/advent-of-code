from functools import reduce

from utils import read_file
game_metadata = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

def is_correct_round(round_data):
    balls = round_data.split(",")
    for ball in balls:
        number, color = ball.split()
        if int(number) > game_metadata[color]:
            return False
    return True

def solve1(data):
    possible_games_ids_sum = 0
    for line in data:
        game_data, rest = line.split(":")
        rounds_data = rest.split(";")
        game_id = int(game_data.split()[-1])
        for round in rounds_data:
            if not is_correct_round(round):
                break
        else:
            possible_games_ids_sum += game_id

    return possible_games_ids_sum

def solve2(data):
    data_power = 0
    for line in data:
        game_data, rest = line.split(":")
        rounds_data = rest.split(";")
        game_id = int(game_data.split()[-1])
        minimum_balls = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        for round in rounds_data:
            balls = round.split(",")
            for ball in balls:
                number, color = ball.split()
                if minimum_balls[color] < int(number):
                    minimum_balls[color] = int(number)

        data_power += reduce(lambda x, y: x*y, minimum_balls.values())

    return data_power



def main():
    file_path = "input.txt"
    data = read_file(file_path)
    print(solve1(data))
    print(solve2(data))


if __name__ == '__main__':
    main()