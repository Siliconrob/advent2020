# from aocd import get_data
import sqlite3
import numpy as np
from datetime import datetime

if __name__ == '__main__':
    data = [
        # "0,3,6"
        "0, 1, 4, 13, 15, 12, 16"
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
    end_number = memory[len(memory) - 1]
    print(f'Part 1: {end_number}')

    # Redo the approach to use in memory database tables because the above method is hours long
    # the below approach is like 5 minutes
    conn = sqlite3.connect(":memory:")
    # Create a single table
    conn.execute('CREATE TABLE "zippers" ("round"	INTEGER, "value"	INTEGER, PRIMARY KEY("round") )')
    conn.execute('CREATE INDEX "ix_val" ON "zippers" ("value")') # this is very necessary

    # Load the data into the table
    rounds = 30000000
    current_index = 0
    for start_number in start_numbers:
        conn.execute(f'INSERT INTO zippers (round, value) VALUES ({current_index}, {start_number})')
        current_index += 1

    cursor = conn.cursor()
    set = 0
    for round in range(current_index, rounds):
        cursor.execute("""select max(a.round) - min(a.round) new_number
                            from 
                            (
                                select round
                                from zippers
                                where value
                                IN 
                                (
                                    select value
                                    from zippers
                                    order by round desc
                                    limit 1
                                )
                                order by round desc
                                limit 2
                            ) a""")
        result = cursor.fetchone()[0]
        conn.execute(f'INSERT INTO zippers (round, value) VALUES ({round}, {result})')
        if round % 10000 == 0:
            print(f'Records done {set * 10000} at {datetime.now().strftime("%H:%M:%S")}')
            set += 1
    cursor.execute("""select VALUE from zippers order by round DESC limit 1""")
    answer = cursor.fetchone()[0]
    print(f'Part 2: {answer}')


