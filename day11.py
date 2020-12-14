from aocd import get_data

class Neighbor:
    def __init__(self, search_x, search_y, x_increment, y_increment):
        self.search_x = search_x
        self.search_y = search_y
        self.x_increment = x_increment
        self.y_increment = y_increment
        self.search_complete = False
        self.result = None

    def nextPosition(self, coord_dict):
        coord = f'{self.search_x + self.x_increment}_{self.search_y + self.y_increment}'
        next_adjacent = coord_dict.get(coord)
        if next_adjacent is not None:
            self.result = next_adjacent
        self.search_x += self.x_increment
        self.search_y += self.y_increment
        if next_adjacent in ["L", "#", None]:
            self.search_complete = True

def flatten_matrix(input_matrix):
    flattened = ""
    for row in input_matrix:
        flattened = flattened + "".join(row)
    return flattened

def print_matrix(input_matrix):
    for row in input_matrix:
        print("".join(row))

def get_visible_neighbors(input_matrix, start_x, start_y):
    d = {
        (f'{inner_x}_{inner_y}'): input_matrix[inner_x][inner_y] for inner_x in range(len(input_matrix)) for inner_y in range(len(input_matrix[0]))
    }

    search_directions = [
        Neighbor(start_x, start_y, 0, -1),  #east
        Neighbor(start_x, start_y, 0, 1),   #west
        Neighbor(start_x, start_y, 1, 0),   #south
        Neighbor(start_x, start_y, -1, 0),  #north
        Neighbor(start_x, start_y, -1, -1), #northwest
        Neighbor(start_x, start_y, 1, -1),  #southwest
        Neighbor(start_x, start_y, 1, 1),   #southeast
        Neighbor(start_x, start_y, -1, 1)   #northeast
    ]

    results = []
    for search_direction in search_directions:
        while True:
            search_direction.nextPosition(d)
            if search_direction.search_complete:
                if search_direction.result is not None:
                    results.append(search_direction.result)
                break
    return results;

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

def seat_passengers_by_visibility(input_matrix):
    output_matrix = []
    x = 0
    for row in input_matrix:
        y = 0
        new_row = []
        for column in row:
            current_seat = input_matrix[x][y]
            next_seat = current_seat
            if current_seat != ".":
                next_seat = current_seat
                current = get_visible_neighbors(input_matrix, x, y)
                adjacent_occupied = list(current).count("#")
                if current_seat == "#" and adjacent_occupied >= 5:
                    next_seat = "L"
                if current_seat == "L" and adjacent_occupied == 0:
                    next_seat = "#"
            new_row.append(next_seat)
            y += 1
        x += 1
        output_matrix.append(new_row)
    return output_matrix

def seat_passengers(input_matrix):
    output_matrix = []
    x = 0
    for row in input_matrix:
        y = 0
        new_row = []
        for column in row:
            current_seat = input_matrix[x][y]
            next_seat = current_seat
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
    return output_matrix

if __name__ == '__main__':
    data = get_data(day=11).splitlines()
    # data_lines = data.splitlines()

    # data = [
    #     "L.LL.LL.LL",
    #     "LLLLLLL.LL",
    #     "L.L.L..L..",
    #     "LLLL.LL.LL",
    #     "L.LL.LL.LL",
    #     "L.LLLLL.LL",
    #     "..L.L.....",
    #     "LLLLLLLLLL",
    #     "L.LLLLLL.L",
    #     "L.LLLLL.LL"
    # ]

    matrix = read_matrix(data)

    index = 0
    previous_run = ""
    filled_seats = 0
    while True:
        matrix = seat_passengers(matrix)
        index += 1
        current_run = flatten_matrix(matrix)
        print(f'Round [{index}]: {current_run}')
        if previous_run == current_run:
            filled_seats = current_run.count("#")
            break
        else:
            previous_run = current_run
    print(f'Part 1: filled seats {filled_seats}')

    while True:
        matrix = seat_passengers_by_visibility(matrix)
        index += 1
        current_run = flatten_matrix(matrix)
        print(f'Round [{index}]: {current_run}')
        if previous_run == current_run:
            filled_seats = current_run.count("#")
            break
        else:
            previous_run = current_run
    print(f'Part 2: filled seats {filled_seats}')

