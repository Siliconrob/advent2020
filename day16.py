from functools import reduce
#from aocd import get_data
import sqlite3
from parse import parse

class InputRule:
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max

class Ticket:
    def __init__(self, ticket_type = "nearby", ids = []):
        self.ticket_type = ticket_type
        self.ids = ids

def parse_rules(input_rules):
    rules = []
    for input_rule in input_rules.split("\n"):
        name, min_rule1, max_rule1, min_rule2, max_rule2 = parse("{}: {:d}-{:d} or {:d}-{:d}", input_rule)
        rules.append(InputRule(name, min_rule1, max_rule1))
        rules.append(InputRule(name, min_rule2, max_rule2))
    return rules

def parse_my_ticket(my_ticket_input):
    ids = [int(number) for number in my_ticket_input.split("\n")[-1].split(',')]
    return Ticket("your ticket", ids)

def parse_nearby_tickets(nearby_ticket_inputs):
    nearby_tickets = []
    for ticket_data in nearby_ticket_inputs.split("\n"):
        if ticket_data.startswith("nearby tickets:"):
            continue
        ids = [int(number) for number in ticket_data.split(',')]
        nearby_tickets.append(Ticket("nearby ticket", ids))
    return nearby_tickets


if __name__ == '__main__':
    data = [
            "class: 0-1 or 4-19\nrow: 0-5 or 8-19\nclass2: 0-13 or 16-19",
            "your ticket:\n11,12,13",
            "nearby tickets:\n3, 9, 18\n15, 1, 5\n5, 14, 9\n22, 4, 5"
    ]

    # data = get_data(day=16).split("\n\n")

    input_rules = parse_rules(data[0])
    conn = sqlite3.connect(":memory:")
    # Create a single table
    conn.execute('CREATE TABLE "ranges" ("name"	TEXT, "min"	INTEGER, "max"	INTEGER )')
    conn.execute('CREATE INDEX "ix_range" ON "ranges" ("min", "max" )')

    cursor = conn.cursor()
    for input_rule in input_rules:
        cursor.execute('INSERT INTO "ranges" ("name", "min", "max") VALUES (:name, :min, :max)', { "name": input_rule.name, "min": input_rule.min, "max": input_rule.max })

    my_ticket = parse_my_ticket(data[1])
    nearby_tickets = parse_nearby_tickets(data[2])

    invalid_scanned_ticket_ids = []
    valid_tickets = []

    for nearby_ticket in nearby_tickets:
        valid_tickets.append(nearby_ticket)
        for id in nearby_ticket.ids:
            cursor.execute("""select name, count(*) matched
                                from ranges
                                where :id between min and max
                                group by name""", { "id": id})
            result = cursor.fetchone()
            if result is None:
                invalid_scanned_ticket_ids.append(id)
                valid_tickets.remove(nearby_ticket)
                break
    scan_error_rate = sum(invalid_scanned_ticket_ids)
    print(f'Part 1: {scan_error_rate}')

    row_data_per_column = []
    for field_index in range(len(valid_tickets[0].ids)):
        row_ids = []
        for valid_ticket in valid_tickets:
            row_ids.append(valid_ticket.ids[field_index])
        row_data_per_column.append(row_ids)

    column_lookup = {}
    column_index = 0
    for row_values in row_data_per_column:
        cursor.execute("""select DISTINCT name from ranges""")
        for field_name in cursor.fetchall():
            search_field = field_name[0]
            if search_field in column_lookup:
                continue
            print(f'Field to search for {search_field}')
            match_count = 0
            for row_id in row_values:
                cursor.execute("""select name from ranges where name = :name and :id between min and max""", {"name": search_field, "id": row_id})
                result = cursor.fetchone()
                if result is not None:
                    match_count += 1
            if match_count == len(row_values):
                column_lookup[search_field] = column_index
                break
        column_index += 1

    departure_columns = {key: val for key, val in column_lookup.items() if key.startswith("class")}
    print(departure_columns)

    departure_tickets = []
    for key, value in departure_columns.items():
        departure_tickets.append(my_ticket.ids[value])

    part2 = reduce((lambda x, y: x * y), departure_tickets)
    print(f'Part 2 answer: {part2}')