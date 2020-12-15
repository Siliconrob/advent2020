# from aocd import get_data
from parse import parse

def rotate_waypoint(input_direction, x_unit, y_unit):
    if input_direction == 90:
        temp = x_unit
        x_unit = y_unit
        y_unit = temp * -1
    if input_direction == 180:
        x_unit = x_unit * -1
        y_unit = y_unit * -1
    if input_direction == 270:
        temp = x_unit
        x_unit = y_unit * -1
        y_unit = temp
    return x_unit, y_unit

if __name__ == '__main__':
    # data = get_data(day=12).splitlines()

    data = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11"
    ]

    # Initial starting point
    current_direction = 90 # face east
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

    current_direction = 0 # Now set point to direction as compass 0
    x_unit, y_unit = 10, 1 # Waypoint
    x, y = 0, 0

    for data_line in data:
        action, move = parse("{}{:d}", data_line)
        print(f'{action} {move}')
        if action == "F":
            x += x_unit * move
            y += y_unit * move
        if action == "N":
            y_unit += move
        if action == "S":
            y_unit -= move
        if action == "E":
            x_unit += move
        if action == "W":
            x_unit -= move
        if action == "R":
            x_unit, y_unit = rotate_waypoint(abs((current_direction + move) % 360), x_unit, y_unit)
        if action == "L":
            x_unit, y_unit = rotate_waypoint(abs((current_direction - move) % 360), x_unit, y_unit)

    manhattan_distance = abs(x) + abs(y)
    print(f'Part 2: Manhattan distance {manhattan_distance}')

