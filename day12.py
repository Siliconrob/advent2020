from parse import parse

if __name__ == '__main__':
    # data = get_data(day=12).splitlines()

    data = [
        "F10",
        "N3",
        "F7",
        "R90",
        "F11"
    ]

    start_orientation = "E"

    manhattan_distance = 0
    for data_line in data:
        action, move = parse("{}{:d}", data_line)
        print(f'{action} {move}')



    print(f'Part 1: Manhattan distance {manhattan_distance}')


