from aocd import get_data
from parse import parse

if __name__ == '__main__':
    data = get_data(day=8)

    # data = [
    #     'nop +0',
    #     'acc +1',
    #     'jmp +4',
    #     'acc +3',
    #     'jmp -3',
    #     'acc -99',
    #     'acc +1',
    #     'jmp -4',
    #     'acc +6'
    # ]

    program = []
    for data_line in data.splitlines():
        instruction, value = parse("{} {:d}", data_line)
        program.append({ "instruction": instruction, "value": value, "count": 0 })

    acc = 0
    current_index = 0
    current_instruction = program[current_index]
    while current_instruction["count"] == 0:
        current_instruction["count"] += 1
        instr = current_instruction["instruction"]
        if instr in ["nop", "acc"]:
            if instr == "acc":
                acc += current_instruction["value"]
            current_index += 1
        if instr == "jmp":
            current_index += (current_instruction["value"])
        current_instruction = program[current_index]

    print(f'Part 1 acc value {acc}')

    # end_node_bags = []
    # graph = {}
    # for data_line in data.splitlines():
    #     bag_line = data_line.split('bags contain')
    #     bag_name = bag_line[0].strip()
    #     contents = bag_line[1].split(",")
    #     inner_bags = []
    #     for inner_bag in contents:
    #         if not inner_bag.strip().startswith("no"):
    #             bag_desc = re.sub("bag[s]?\.?", "", inner_bag)
    #             cleaned_bag_desc = bag_desc.strip()
    #             count, inner_bag_name = parse("{:d} {}", cleaned_bag_desc)
    #             inner_bags.append({ "bag": inner_bag_name, "count": count})
    #         else:
    #             end_node_bags.append(bag_name)
    #     graph[bag_name] = inner_bags