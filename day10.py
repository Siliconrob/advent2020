from aocd import get_data
import networkx as nx
import multiprocessing as mp
import datetime

def count_valid(input_path):
    sort_test = input_path[:]
    sort_test.sort()
    if input_path == sort_test:
        return True
    return False


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

    # data = [
    #     16,
    #     10,
    #     15,
    #     5,
    #     1,
    #     11,
    #     7,
    #     19,
    #     6,
    #     12,
    #     4
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

    current_voltage = 0
    data.insert(0, current_voltage)

    g = nx.DiGraph()

    for start_voltage in data:
        next_voltages = list(filter(lambda number: start_voltage + 3 >= number, data))
        for next_voltage in next_voltages:
            if next_voltage != start_voltage:
                g.add_edge(start_voltage, next_voltage, weight=1)
    count = 0
    found_paths = []

    print(datetime.datetime.utcnow())
    pool = mp.Pool(mp.cpu_count() * 2)
    results = pool.map(count_valid, [path for path in nx.all_simple_paths(g, source=0, target=data[-1])])
    pool.close()
    print(datetime.datetime.utcnow())
    print(f'Paths {results.count(True)}')

    # for path in nx.all_simple_paths(g, source=0, target=data[-1]):
    #     sort_test = path[:]
    #     sort_test.sort()
    #     if path == sort_test:
    #         found_paths.append(path)
    #     print(len(found_paths))
    # print(f'Paths {len(found_paths)}')
