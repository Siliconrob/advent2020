# from aocd import get_data
import numpy as np
from datetime import datetime

if __name__ == '__main__':
    data = [
        "0,3,6"
        # "1,3,2"
    ]

    rounds = 2020
    start_numbers = [int(x) for x in data[0].split(",")]
    current_index = 0
    memory = []
    # Start numbers
    for start_number in start_numbers:
        memory.append(start_number)
        current_index += 1

    # Play game
    for round in range(current_index, rounds):
        last_number = memory[round - 1]
        lookup = np.array(memory)
        found_elements = np.where(lookup == last_number)[0]
        if len(found_elements) == 1:
            memory.append(0)
        else:
            reversed = found_elements.tolist()[::-1]
            new_number = reversed[0] - reversed[1]
            memory.append(new_number)
        if round % 1000 == 0:
            print(f'{datetime.now().strftime("%H:%M:%S")}')
    end_number = memory[len(memory) - 1]
    print(f'Part 1: {end_number}')