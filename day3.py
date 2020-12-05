from aocd import get_data
import math

class Slope:
    def __init__(self, left, down):
        self.down = down
        self.left = left
    trees = 0
    down = 1
    left = 1


if __name__ == '__main__':
    data = get_data(day=3)
    data_lines = data.splitlines()

    x = 0
    trees = 0
    left = 3
    '''
    .#..............##....#.#.####.
    ##..........#.....##...........
    .......#....##...........#.#...
    '''
    for current_line in data_lines:
        line_length = len(current_line)
        next_position = x % line_length
        char_to_check = current_line[next_position]
        if char_to_check == '#':
            trees += 1
        x += left

    print(f'Trees Part 1: {trees}')

    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]
    
    for slope in slopes:
        x = 0
        for i in range(0, len(data_lines), slope.down):
            current_line = data_lines[i]
            line_length = len(current_line)
            next_position = x % line_length
            char_to_check = current_line[next_position]
            if char_to_check == '#':
                slope.trees += 1
            x += slope.left
        print(f'Trees Slope ({slope.left}, {slope.down}): {slope.trees}')

    print(f'Trees Part 2: {math.prod([slope.trees for slope in slopes])}')
