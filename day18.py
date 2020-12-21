# from aocd import get_data
import re
import queue

def compute(expression_queue):
    result = None
    math_operand = None
    while not expression_queue.empty():
        next_arg = expression_queue.get()
        if next_arg in ['(',')', ' ']:
            continue
        if result is None:
            result = int(next_arg)
            continue
        if next_arg in ['*', '+']:
            math_operand = next_arg
            continue
        if math_operand == "*":
            result = result * int(next_arg)
        else:
            result = result + int(next_arg)
    return result

def to_queue(expression):
    current = queue.Queue()
    for operand in expression.replace('(','').replace(')','').split(' '):
        current.put(operand)
    return current

if __name__ == '__main__':
    data = [
        "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2",
        "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
        "5 + (8 * 3 + 9 + 3 * 4 * 3)",
        "2 * 3 + (4 * 5)",
        "1 + 2 * 3 + 4 * 5 + 6",
        "1 + (2 * 3) + (4 * (5 + 6))"
    ]
    # data = get_data(day=18).splitlines()

    expression_values = []

    for data_line in data:
        while re.match("^.*[\\(\\)].*$", data_line):
            last_open_paren = -1
            for index in range(len(data_line)):
                current_char = data_line[index]
                if current_char == " ":
                    continue
                if current_char == "(":
                    last_open_paren = index
                if current_char == ")" and last_open_paren > -1:
                    sub_expression = data_line[last_open_paren:index + 1]
                    sub_expression_value = compute(to_queue(sub_expression))
                    data_line = data_line.replace(sub_expression, str(sub_expression_value))
                    print(data_line)
                    break
        print(data_line)
        expression_value = compute(to_queue(data_line))
        expression_values.append(expression_value)

    part1 = sum(expression_values)
    print(f'Part 1: {part1}')