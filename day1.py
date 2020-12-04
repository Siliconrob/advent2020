from aocd import get_data
import sqlite3

if __name__ == '__main__':
    data = get_data(day=1)

    conn = sqlite3.connect(":memory:")
    # Create a single table
    conn.execute('CREATE TABLE "numbers" ("data" INTEGER)')

    # Load the data into the table
    for x in data.splitlines():
        conn.execute(f'INSERT INTO numbers (data) VALUES ({x})')

    cursor = conn.cursor()

    cursor.execute("""SELECT DISTINCT n1.data * n2.data as answer
                        from numbers n1
                        join numbers n2
                        where n1.data <> n2.data
                        and (n1.data + n2.data) = 2020""")
    result = cursor.fetchone()[0]
    print(f'Part 1 answer {result}')

    cursor.execute("""SELECT DISTINCT n1.data * n2.data * n3.data as answer
                        from numbers n1
                        join numbers n2
                        join numbers n3
                        where n1.data <> n2.data <> n3.data
                        and (n1.data + n2.data + n3.data) = 2020""")
    result = cursor.fetchone()[0]
    print(f'Part 2 answer {result}')