from aocd import get_data
from parse import parse
import re

class Passport:
    def __init__(self):
        self.raw_data_lines = []

    def dataLines(self):
        lines = " ".join(self.raw_data_lines).replace('\n', ' ').split(' ')
        return [line.strip(' ') for line in lines]

    def isValidHeight(self, line):
        field_name, field_data = parse("{}:{}", line)
        if field_name != 'hgt':
            return False
        height, unit = parse("{:d}{}", field_data)
        if unit == 'cm' and 150 <= height <= 193:
            return True
        if unit == 'in' and 59 <= height <= 76:
            return True
        return False

    def isValidYear(self, line, match_field, min, max):
        field_name, field_data = parse("{}:{}", line)
        if field_name != match_field:
            return False
        year = parse("{:d}", field_data)[0]
        if min <= year <= max:
            return True
        return False

    def isValidFieldByRegex(self, line, match_field, regex_pattern):
        field_name, field_data = parse("{}:{}", line)
        if field_name != match_field:
            return False
        match = re.match(regex_pattern, field_data)
        return match

    def isValidEyeColor(self, line):
        colors = [
            'amb',
            'blu',
            'brn',
            'gry',
            'grn',
            'hzl',
            'oth'
        ]
        field_name, field_data = parse("{}:{}", line)
        if field_name != 'ecl':
            return False
        if field_data in colors:
            return True
        return False

    def isValidPart2(self):
        valid_fields = 0
        lines = self.dataLines()
        for line in lines:
            if self.isValidYear(line, 'byr', 1920, 2002):
                valid_fields += 1
            if self.isValidYear(line, 'iyr', 2010, 2020):
                valid_fields += 1
            if self.isValidYear(line, 'eyr', 2020, 2030):
                valid_fields += 1
            if self.isValidHeight(line):
                valid_fields += 1
            if self.isValidFieldByRegex(line, 'hcl', '#[a-f0-9]{6}'):
                valid_fields += 1
            if self.isValidFieldByRegex(line, 'pid', '[0-9]{9}'):
                valid_fields += 1
            if self.isValidEyeColor(line):
                valid_fields += 1

        return valid_fields == 7

    def isValidPart1(self):

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

    test = Passport()
    test.raw_data_lines = [
        'eyr:1972 cid:100',
        'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926'
    ]

    result = test.isValidPart2()



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

    valid_passports_part1 = 0
    valid_passports_part2 = 0

    for passport in passports:
        if passport.isValidPart1():
            valid_passports_part1 += 1
        if passport.isValidPart2():
            valid_passports_part2 += 1

    print(f'Part 1: Valid Passports {valid_passports_part1}')
    print(f'Part 2: Valid Passports {valid_passports_part2}')
