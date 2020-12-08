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
    possible_changes = []

    current_instruction = program[current_index]
    while current_instruction["count"] == 0 or current_index > len(program):
        current_instruction["count"] += 1
        instr = current_instruction["instruction"]
        if instr in ["nop", "acc"]:
            if instr == "acc":
                acc += current_instruction["value"]
            else:
                possible_changes.append({"instr": "nop", "index": current_index})
            current_index += 1
        if instr == "jmp":
            possible_changes.append({"instr": "jmp", "index": current_index})
            current_index += (current_instruction["value"])
        current_instruction = program[current_index]

    print(f'Part 1 acc value {acc}')

    for possible_change in possible_changes:
        program.clear()
        for data_line in data.splitlines():
            instruction, value = parse("{} {:d}", data_line)
            program.append({"instruction": instruction, "value": value, "count": 0})
        index = possible_change["index"]
        previous_cmd = program[index]["instruction"]
        if possible_change["instr"] == "nop":
            program[index]["instruction"] = "jmp"
        else:
            program[index]["instruction"] = "nop"
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
            try:
                current_instruction = program[current_index]
            except:
                new_instr = program[index]["instruction"]
                print(f"Change {index} from {previous_cmd} to {new_instr}")
                print(f'Part 2 acc value {acc}')