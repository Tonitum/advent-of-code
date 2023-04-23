#!/usr/bin/python3
from aoc.utilities.parsing import load_input

def parse_input(input_data: list) -> list:
    parsed_data = []
    elf_index = 0
    temp_list = []
    for line in input_data:
        if line == "\n":
            parsed_data.append(temp_list)
            temp_list = []
            continue
        temp_list.append(int(line.strip("\n")))
    if temp_list:
        parsed_data.append(temp_list)
    return parsed_data


def sum_groups(sorted_list: list) -> list:
    summed_groups = []
    for group in sorted_list: 
        summed_groups.append(sum(group))
    return summed_groups


def find_largest(sums: list) -> int:
    max_1 = max(sums)
    sums.remove(max_1)
    max_2 = max(sums)
    sums.remove(max_2)
    max_3 = max(sums)
    return max_1 + max_2 + max_3
 

def main():
    # load the input
    elf_data = load_input("~/projects/tonitum/aoc/day1/input.txt")
    # parse the input, separating into groups
    sorted_list = parse_input(elf_data)
    # sum the groups
    summed_groups = sum_groups(sorted_list)
    # return largest
    print(find_largest(summed_groups))

if __name__ == "__main__":
    main()
