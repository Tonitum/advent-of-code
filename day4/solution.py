#!/usr/bin/python3
import os
from aoc.utilities.parsing import load_input


def parse_input_1(input_data: list) -> list:
    parsed_data = []
    elf_index = 0
    temp_list = []
    for line in input_data:
        line = line.strip("\n")
        # split by comma
        pairs = line.split(",")

        # split each set by -
        temp_list.append(pairs[0].split("-"))
        temp_list.append(pairs[1].split("-"))
        parsed_data.append(temp_list)
        temp_list = []
    return parsed_data


def main():
    tonitum = os.environ.get('TONITUM')
    day = 4
    input_file_name = 'input.txt'
    # input_file_name = 'test_input.txt'
    input_path = os.path.abspath(f'{tonitum}/aoc/day{day}/{input_file_name}')
    data = load_input(input_path)
    parsed_data = parse_input_1(data)
    contain_count = 0
    for pair in parsed_data:
        elf_1_min = int(pair[0][0])
        elf_1_max = int(pair[0][1])
        elf_2_min = int(pair[1][0])
        elf_2_max = int(pair[1][1])

        if (elf_1_min <= elf_2_min) and (elf_1_max >= elf_2_max):
            contain_count = contain_count + 1
            continue
        elif (elf_2_min <= elf_1_min) and (elf_2_max >= elf_1_max):
            contain_count = contain_count + 1
            continue
    print(contain_count)
    overlap_count = 0
    for pair in parsed_data:
        elf_1_min = int(pair[0][0])
        elf_1_max = int(pair[0][1])
        elf_2_min = int(pair[1][0])
        elf_2_max = int(pair[1][1])

        if elf_1_min in range(elf_2_min,elf_2_max+1):
            overlap_count = overlap_count + 1
        elif elf_1_max in range(elf_2_min,elf_2_max+1):
            overlap_count = overlap_count + 1
        elif elf_2_min in range(elf_1_min,elf_1_max+1):
            overlap_count = overlap_count + 1
        elif elf_2_max in range(elf_1_min,elf_1_max+1):
            overlap_count = overlap_count + 1
    print(overlap_count)




if __name__ == "__main__":
    main()
