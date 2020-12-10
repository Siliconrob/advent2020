from aocd import get_data
from parse import parse

if __name__ == '__main__':
    # data = [
    #     28,
    #     33,
    #     18,
    #     42,
    #     31,
    #     14,
    #     46,
    #     20,
    #     48,
    #     47,
    #     24,
    #     23,
    #     49,
    #     45,
    #     19,
    #     38,
    #     39,
    #     11,
    #     1,
    #     32,
    #     25,
    #     35,
    #     8,
    #     17,
    #     7,
    #     9,
    #     4,
    #     2,
    #     34,
    #     10,
    #     3
    # ]

    data = [int(line_data) for line_data in get_data(day=10).splitlines()]
    data.sort()
    device_adapter_volts = data[-1] + 3
    data.append(device_adapter_volts)
    current_voltage = 0

    volt_diffs = []
    for next_voltage in data:
        volt_diffs.append(next_voltage - current_voltage)
        current_voltage = next_voltage

    print(f'1 volt diffs {volt_diffs.count(1)} 3 volt diffs {volt_diffs.count(3)}')
    print(f'Part 1 answer {volt_diffs.count(1) * volt_diffs.count(3)}')
