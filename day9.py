from aocd import get_data
from parse import parse

def generate_options(input_numbers):
    options = []
    start = 0
    while start < len(input_numbers):
        index = start + 1
        while index < len(input_numbers):
            result = input_numbers[start] + input_numbers[index]
            options.append(result)
            index += 1
        start += 1
    return options

def find_range(input_numbers, target):
    start = 0
    sum_list = []
    while start < len(input_numbers):
        sum_list = []
        index = start
        while sum(sum_list) < target:
            sum_list.append(input_numbers[index])
            index += 1
        if sum(sum_list) == target:
            break
        start += 1
    return sum_list

if __name__ == '__main__':
    # data = [
    #     35,
    #     20,
    #     15,
    #     25,
    #     47,
    #     40,
    #     62,
    #     55,
    #     65,
    #     95,
    #     102,
    #     117,
    #     150,
    #     182,
    #     127,
    #     219,
    #     299,
    #     277,
    #     309,
    #     576
    # ]

    data = [int(line_data) for line_data in get_data(day=9).splitlines()]
    preamble_length = 25
    # preamble_length = 5
    current_index = 0
    while current_index < len(data):
        current_value = data[current_index + preamble_length]
        input_list = data[current_index:current_index + preamble_length]
        options = generate_options(input_list)
        if current_value not in options:
            break
        current_index += 1
    print(f'Part 1 answer {current_value}')

    found_range = find_range(data[0:current_index + preamble_length], current_value)
    print(f'Part 2 answer {min(found_range) + max(found_range)}')
