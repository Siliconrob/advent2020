# from aocd import get_data
from parse import parse
from functools import reduce

def parse_input(data_lines):
    start_time = parse("{:d}", data[0])[0]
    times = []
    for time in data[1].split(","):
        parsed_time = parse("{:d}", time)
        if parsed_time is not None:
            times.append(parsed_time[0])
    return start_time, times

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__ == '__main__':
    # data = get_data(day=13).splitlines()
    # data = [
    #     "939",
    #     "7, 13, x, x, 59, x, 31, 19"
    # ]

    data = [
        "1011416",
        "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,911,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,827,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19"
    ]

    start_time, times = parse_input(data)
    bus_starts = {}
    for bus_time in times:
        bus_starts[bus_time] = start_time - (start_time % bus_time) + bus_time
    first_bus = sorted(bus_starts, key=bus_starts.get)[0]
    part1 = first_bus * (bus_starts[first_bus] - start_time)
    print(f'Part 1: {part1}')

    buses = [int(number) if number != 'x' else 'x' for number in data[1].split(',')]

    # Part 2
    all_buses = []
    differences = []
    for index, bus in enumerate(buses):
        if bus == "x":
            continue
        all_buses.append(bus)
        differences.append(bus - index)

    print(f'Part 2: {chinese_remainder(all_buses, differences)}')

