# from aocd import get_data
import sqlite3
from datetime import datetime
from parse import parse

class InputRule:
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

class Ticket:
    def __init__(self, name, ids):
        self.name = name
        self.ids

if __name__ == '__main__':
    data = [
        "class: 1 - 3 or 5 - 7",
        "row: 6 - 11 or 33 - 44",
        "seat: 13 - 40 or 45 - 50",
        "",
        "your ticket:",
        "7, 1, 14",
        "",
        "nearby tickets:",
        "7, 3, 47",
        "40, 4, 50",
        "55, 2, 20",
        "38, 6, 12"
    ]

    # data = get_data(day=16).split("\n\n")


    for data_line in data:
        print(data_line)


    # # Redo the approach to use in memory database tables because the above method is hours long
    # # the below approach is like 5 minutes
    # conn = sqlite3.connect(":memory:")
    # # Create a single table
    # conn.execute('CREATE TABLE "zippers" ("round"	INTEGER, "value"	INTEGER, PRIMARY KEY("round") )')
    # conn.execute('CREATE INDEX "ix_val" ON "zippers" ("value")') # this is very necessary
    #
    # # Load the data into the table
    # rounds = 30000000
    # current_index = 0
    # for start_number in start_numbers:
    #     conn.execute(f'INSERT INTO zippers (round, value) VALUES ({current_index}, {start_number})')
    #     current_index += 1
    #
    # cursor = conn.cursor()
    # set = 0
    # for round in range(current_index, rounds):
    #     cursor.execute("""select max(a.round) - min(a.round) new_number
    #                         from
    #                         (
    #                             select round
    #                             from zippers
    #                             where value
    #                             IN
    #                             (
    #                                 select value
    #                                 from zippers
    #                                 order by round desc
    #                                 limit 1
    #                             )
    #                             order by round desc
    #                             limit 2
    #                         ) a""")
    #     result = cursor.fetchone()[0]
    #     conn.execute(f'INSERT INTO zippers (round, value) VALUES ({round}, {result})')
    #     if round % 10000 == 0:
    #         print(f'Records done {set * 10000} at {datetime.now().strftime("%H:%M:%S")}')
    #         set += 1
    # cursor.execute("""select VALUE from zippers order by round DESC limit 1""")
    # answer = cursor.fetchone()[0]
    # print(f'Part 2: {answer}')


