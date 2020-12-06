from aocd import get_data

if __name__ == '__main__':
    data = get_data(day=6)
    passenger_groups = data.split("\n\n")
    answer_groups = []
    for passenger_group in passenger_groups:
        passenger_answers = dict()
        for passenger_group_line in passenger_group.splitlines():
            for char_answer in passenger_group_line:
                if char_answer not in passenger_answers:
                    passenger_answers[char_answer] = 1
        answer_groups.append(len(passenger_answers.keys()))

    print(f'Part 1 answer: {sum(answer_groups)}')
