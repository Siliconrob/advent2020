# from aocd import get_data
from parse import *

def apply_mask(mask, bin_value):
    masked_value = []
    for index in range(len(mask)):
        bit = mask[index]
        new_bit_value = bin_value[index]
        if bit != "X":
            new_bit_value = bit
        masked_value.append(new_bit_value)
    masked = "".join(masked_value)
    return int(masked, 2)

if __name__ == '__main__':
    # data = get_data(day=13).splitlines()
    data = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[58] = 11",
        "mem[7] = 101",
        "mem[58] = 0"
    ]

    mem_values = {}
    for data_line in data:
        if data_line.startswith("mask"):
            mask = parse("mask = {}", data_line)[0]
        else:
            mem_location, dec_value = parse("mem[{:d}] = {:d}", data_line)
            bin_value = bin(dec_value).replace("0b", "").zfill(len(mask))
            mem_values[mem_location] = apply_mask(mask, bin_value)
    print(f'Part 1 answer {sum(list(mem_values.values()))}')