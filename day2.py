from aocd import get_data
from parse import parse
import sqlite3

if __name__ == '__main__':
    data = get_data(day=2)

    conn = sqlite3.connect(":memory:")
    # Create a single table
    conn.execute("""CREATE TABLE IF NOT EXISTS "passwords" (
                    "Data"	TEXT,
                    "CharToFind"	TEXT,
                    "Min"	INTEGER,
                    "Max"	INTEGER
                )""")

    # Load the data into the table
    for dataLine in data.splitlines():
        min, max, charToFind, data = parse("{:d}-{:d} {}: {}", dataLine)
        sql = f'INSERT INTO passwords ([Min], [Max], [CharToFind],[data]) VALUES ({min}, {max}, \'{charToFind}\', \'{data})\')'
        conn.execute(sql)

    cursor = conn.cursor()
    cursor.execute("""SELECT COUNT(*)
                        FROM passwords
                        WHERE length(data) - length(replace(data, CharToFind, '')) between min and max""")
    result = cursor.fetchone()[0]
    print(f'Part 1 answer {result}')

    cursor.execute("""SELECT COUNT(*)
                        FROM passwords
                        WHERE substr(data, min, 1) = CharToFind
                        AND substr(data,max, 1) <> CharToFind""")

    result = cursor.fetchone()[0]
    print(f'Part 2 answer {result}')
