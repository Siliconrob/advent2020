from aocd import get_data
import re
from parse import parse

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath

if __name__ == '__main__':
    data = get_data(day=7)

    # data = [
    #     'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    #     'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    #     'bright white bags contain 1 shiny gold bag.',
    #     'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    #     'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    #     'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    #     'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    #     'faded blue bags contain no other bags.',
    #     'dotted black bags contain no other bags.'
    # ]

    graph = {}
    for data_line in data.splitlines():
        bag_line = data_line.split('bags contain')
        bag_name = bag_line[0].rstrip().lstrip()
        contents = bag_line[1].split(",")
        inner_bags = []
        for inner_bag in contents:
            if not inner_bag.rstrip().lstrip().startswith("no"):
                bag_desc = re.sub("bag[s]?\.?", "", inner_bag)
                cleaned_bag_desc = bag_desc.rstrip().lstrip()
                count, inner_bag_name = parse("{:d} {}", cleaned_bag_desc)
                inner_bags.append(inner_bag_name)
        graph[bag_name] = inner_bags

    bag_to_find = "shiny gold"
    valid_paths = 0
    for start_node in graph.keys():
        path = find_path(graph, start_node, bag_to_find)
        if path is not None and len(path) > 1:
            print(path)
            valid_paths += 1
    print(f'Bags containing {bag_to_find}: {valid_paths}')

