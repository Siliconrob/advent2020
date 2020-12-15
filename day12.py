from aocd import get_data
from parse import parse

if __name__ == '__main__':
    data = get_data(day=12).splitlines()

    # data = [
    #     "F10",
    #     "N3",
    #     "F7",
    #     "R90",
    #     "F11"
    # ]

    current_direction = 90
    x, y = 0, 0

    for data_line in data:
        action, move = parse("{}{:d}", data_line)
        print(f'{action} {move}')
        if action == "F":
            if current_direction == 90:
                x += move
            if current_direction == 180:
                y -= move
            if current_direction == 0:
                y += move
            if current_direction == 270:
                x -= move
        if action == "R":
            current_direction = abs((current_direction + move) % 360)
        if action == "L":
            current_direction = abs((current_direction - move) % 360)
        if action == "N":
            y += move
        if action == "S":
            y -= move
        if action == "E":
            x += move
        if action == "W":
            x -= move

    manhattan_distance = abs(x) + abs(y)
    print(f'Part 1: Manhattan distance {manhattan_distance}')


