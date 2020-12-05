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

    seat_ids = []
    for data_line in data_lines:
        row = findPosition(dataQueue(data_line, 0, 7), 'B', 0, 127)
        column = findPosition(dataQueue(data_line, 7), 'R', 0, 7)
        seat_ids.append(row * 8 + column)
    print(f'Part 1: SeatId {max(seat_ids)}')

    seat_ids.sort()
    seat_ids.reverse()
    previous_seat_id = seat_ids[0]
    my_seat_id = previous_seat_id
    for current_seat_id in seat_ids:
        if previous_seat_id - current_seat_id > 1:
            my_seat_id = current_seat_id + 1
            break
        previous_seat_id = current_seat_id
    print(f'Part 2: My SeatId {my_seat_id}')
