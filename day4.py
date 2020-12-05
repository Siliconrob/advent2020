from aocd import get_data
from parse import parse

class Passport:
    def __init__(self):
        self.raw_data_lines = []

    def dataLines(self):
        lines = " ".join(self.raw_data_lines).replace('\n', ' ').split(' ')
        return [line.strip(' ') for line in lines]

    def isValid(self):

        required_fields = [
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid'
        ]
        lines = self.dataLines()
        valid_fields = 0
        for line in lines:
            field_name, field_data = parse("{}:{}", line)
            if field_name in required_fields:
                valid_fields += 1
        if valid_fields == 7:
            return True
        return False

    raw_data_lines = []


if __name__ == '__main__':
    data = get_data(day=4)
    data_lines = data.splitlines()
    passports = []
    currentPassport = Passport()
    for current_line in data_lines:
        if current_line == '':
            passports.append(currentPassport)
            currentPassport = Passport()
        else:
            currentPassport.raw_data_lines.append(current_line)

    valid_passports = 0

    for passport in passports:
        if passport.isValid():
            valid_passports += 1

    print(f'Part 1: Valid Passports {valid_passports}')
