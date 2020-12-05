from aocd import get_data
import queue

def dataQueue(line, start, end = 0):
    if end > 0:
        input = line[start:end]
    else:
        input = line[start:]
    queue_data = queue.Queue()
    for item in input:
        queue_data.put(item)
    return queue_data

def findPosition(queue_data, upperIndicatorChar, start, end):
    while not queue_data.empty():
        moveDirection = queue_data.get()
        diff = int((end - start) / 2)
        if moveDirection == upperIndicatorChar:
            start += diff + 1
        else:
            end -= diff + 1
    return start

if __name__ == '__main__':
    data = get_data(day=5)
    data_lines = data.splitlines()

    seat_id = 0
    for data_line in data_lines:
        row = findPosition(dataQueue(data_line, 0, 7), 'B', 0, 127)
        column = findPosition(dataQueue(data_line, 7), 'R', 0, 7)
        new_seat_id = row * 8 + column
        if new_seat_id > seat_id:
            seat_id = new_seat_id
    print(f'Part 1: SeatId {seat_id}')
