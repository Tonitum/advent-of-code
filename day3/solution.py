#!/usr/bin/python3
import os

from aoc.utilities.parsing import load_input

CHAR_SCORE = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def parse_input_1(input_data: list) -> list:
    parsed_data = []
    elf_index = 0
    temp_list = []
    for line in input_data:
        line = line.strip("\n")
        part_length = int(len(line) / 2)
        part1 = line[0:part_length]
        part2 = line[part_length:]
        temp_list.append(part1)
        temp_list.append(part2)
        parsed_data.append(temp_list)
        temp_list = []
    return parsed_data


def parse_input_2(input_data: list) -> list:
    parsed_data = []
    elf_index = 0
    temp_list = []
    for line in input_data:
        line = line.strip("\n")
        if len(temp_list) == 3:
            parsed_data.append(temp_list)
            temp_list = []
        temp_list.append(line)
    if temp_list is not []:
        parsed_data.append(temp_list)
    return parsed_data


def main():
    tonitum = os.environ.get('TONITUM')
    input_path = os.path.abspath(f'{tonitum}/aoc/day3/input.txt')
    # input_path = os.path.abspath(f'{tonitum}/aoc/day3/test_input.txt')

    data = load_input(input_path)
    parsed_data = parse_input_1(data)
    total = 0
    for item_pair in parsed_data:
        common_item = set(item_pair[0]) & set(item_pair[1])
        total = total + CHAR_SCORE.find(common_item.pop()) + 1
    # print(total)
    group_total = 0
    parsed_data_2 = parse_input_2(data)
    for elf_group in parsed_data_2:
        elf_set_1 = set(elf_group[0])
        elf_set_2 = set(elf_group[1])
        elf_set_3 = set(elf_group[2])
        common_set = elf_set_1 & elf_set_2 & elf_set_3
        group_total = group_total + CHAR_SCORE.find(common_set.pop()) + 1
    print(group_total)


if __name__ == "__main__":
    main()
