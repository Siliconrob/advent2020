from aocd import get_data
import queue

def print_matrix(input_matrix):
    for row in input_matrix:
        print("".join(row))

def get_neighbors(input_matrix, start_x, start_y):
    d = {
        (inner_x, inner_y): input_matrix[inner_x][inner_y] for inner_x in range(len(input_matrix)) for inner_y in range(len(input_matrix[0]))
    }
    return filter(None, [
        d.get(i) for i in
        [
            (start_x + 1, start_y + 1),
            (start_x, start_y + 1),
            (start_x + 1, start_y),
            (start_x - 1, start_y + 1),
            (start_x - 1, start_y),
            (start_x, start_y - 1),
            (start_x + 1, start_y - 1),
            (start_x - 1, start_y - 1)
        ]
    ])


def read_matrix(data):
    matrix = []
    for data_line in data:
        new_row = []
        for seat_description in data_line:
            new_row.append(seat_description)
        matrix.append(new_row)
    return matrix


def seat_passengers(input_matrix):
    output_matrix = []
    x = 0
    for row in input_matrix:
        y = 0
        new_row = []
        for column in row:
            current_seat = input_matrix[x][y]
            next_seat = "."
            if current_seat != ".":
                next_seat = current_seat
                current = get_neighbors(input_matrix, x, y)
                adjacent_occupied = list(current).count("#")
                if current_seat == "#" and adjacent_occupied >= 4:
                    next_seat = "L"
                if current_seat == "L" and adjacent_occupied == 0:
                    next_seat = "#"
            new_row.append(next_seat)
            y += 1
        x += 1
        output_matrix.append(new_row)
    print_matrix(output_matrix)
    return output_matrix

if __name__ == '__main__':
    # data = get_data(day=10)
    # data_lines = data.splitlines()

    data = [
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL"
    ]

    matrix = read_matrix(data)

    filled_seats = 0
    previous_compare = ""
    while True:
        results = seat_passengers(matrix)
        new_compare = "".join([item for sublist in results for item in sublist])
        if previous_compare == new_compare:
            filled_seats = new_compare.count("#")
            break
        previous_compare = new_compare
        print_matrix(results)
        print('break')
    print(f'Part 1: filled seats {filled_seats}')
