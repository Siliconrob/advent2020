from aocd import get_data

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
