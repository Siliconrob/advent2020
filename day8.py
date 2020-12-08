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

    jmps = []
    nops = []

    current_instruction = program[current_index]
    while current_instruction["count"] == 0 or current_index > len(program):
        current_instruction["count"] += 1
        instr = current_instruction["instruction"]
        if instr in ["nop", "acc"]:
            if instr == "acc":
                acc += current_instruction["value"]
            else:
                nops.append(current_index)
            current_index += 1
        if instr == "jmp":
            jmps.append(current_index)
            current_index += (current_instruction["value"])
        current_instruction = program[current_index]

    print(f'Part 1 acc value {acc}')

    for nop in nops:
        program.clear()
        for data_line in data.splitlines():
            instruction, value = parse("{} {:d}", data_line)
            program.append({"instruction": instruction, "value": value, "count": 0})
        program[nop]["instruction"] = "jmp"

        acc = 0
        current_index = 0
        current_instruction = program[current_index]
        if current_index > len(program):
            print(f"Change {nop} {acc}")
            break
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
                print(f"Change index changed nop to jmp {nop} {acc}")

    for jmp in jmps:
        program.clear()
        for data_line in data.splitlines():
            instruction, value = parse("{} {:d}", data_line)
            program.append({"instruction": instruction, "value": value, "count": 0})
        program[jmp]["instruction"] = "nop"

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
                print(f"Change index changed jmp to nop {jmp}")
                print(f'Part 2 acc value {acc}')