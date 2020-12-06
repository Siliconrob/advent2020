from aocd import get_data

if __name__ == '__main__':
    data = get_data(day=6)
    passenger_groups = data.split("\n\n")
    all_answer_groups = []
    answer_groups = []
    for passenger_group in passenger_groups:
        passenger_answers = dict()
        passenger_group_lines = passenger_group.splitlines()
        for passenger_group_line in passenger_group_lines:
            for char_answer in passenger_group_line:
                if char_answer not in passenger_answers:
                    passenger_answers[char_answer] = 1
                else:
                    passenger_answers[char_answer] += 1

        answer_groups.append(len(passenger_answers.keys()))
        all_answered = {k: v for (k, v) in passenger_answers.items() if v == len(passenger_group_lines)}
        all_answer_groups.append(len(all_answered.keys()))

    print(f'Part 1 answer: {sum(answer_groups)}')
    print(f'Part 2 answer: {sum(all_answer_groups)}')
