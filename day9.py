from aocd import get_data
from parse import parse

if __name__ == '__main__':
    data = get_data(day=9)

    for data_line in data.splitlines():
        print(data_line)