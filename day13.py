# from aocd import get_data
from parse import parse

def parse_input(data_lines):
    start_time = parse("{:d}", data[0])[0]
    times = []
    for time in data[1].split(","):
        parsed_time = parse("{:d}", time)
        if parsed_time is not None:
            times.append(parsed_time[0])
    return start_time, times

if __name__ == '__main__':
    # data = get_data(day=13).splitlines()
    data = [
        "939",
        "7, 13, x, x, 59, x, 31, 19"
    ]
    start_time, times = parse_input(data)
    bus_starts = {}
    for bus_time in times:
        bus_starts[bus_time] = start_time - (start_time % bus_time) + bus_time
    first_bus = sorted(bus_starts, key=bus_starts.get)[0]
    part1 = first_bus * (bus_starts[first_bus] - start_time)
    print(f'Part 1: First_Bus {part1}')
