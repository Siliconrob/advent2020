# from aocd import get_data
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
    for input_rule in input_rules:
        name, min_rule1, max_rule1, min_rule2, max_rule2 = parse("{}: {:d}-{:d} or {:d}-{:d}", input_rule)
        rules.append(InputRule(name, min_rule1, max_rule1))
        rules.append(InputRule(name, min_rule2, max_rule2))
    return rules

def parse_my_ticket(my_ticket_input):
    ids = [int(number) for number in my_ticket_input[-1].split(',')]
    return Ticket("your ticket", ids)

def parse_nearby_tickets(nearby_ticket_inputs):
    nearby_tickets = []
    for ticket_data in nearby_ticket_inputs:
        if ticket_data.startswith("nearby tickets:"):
            continue
        ids = [int(number) for number in ticket_data.split(',')]
        nearby_tickets.append(Ticket("nearby ticket", ids))
    return nearby_tickets


if __name__ == '__main__':
    data = [
        [
            "class: 1-3 or 5-7",
            "row: 6-11 or 33-44",
            "seat: 13-40 or 45-50"
        ],
        [
            "your ticket:",
            "7, 1, 14"
        ],
        [
            "nearby tickets:",
            "7, 3, 47",
            "40, 4, 50",
            "55, 2, 20",
            "38, 6, 12"
        ]
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
    for nearby_ticket in nearby_tickets:
        for id in nearby_ticket.ids:
            cursor.execute("""select name, count(*) matched
                                from ranges
                                where :id between min and max
                                group by name""", { "id": id})
            result = cursor.fetchone()
            if result is None:
                invalid_scanned_ticket_ids.append(id)
                break
    scan_error_rate = sum(invalid_scanned_ticket_ids)
    print(f'Part 1: {scan_error_rate}')


