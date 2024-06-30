from typing import Tuple
from utilities.day import Day

class DayThree(Day):
    def get_relative_chars(self, line: str, pos: int) -> str:
        # get the char to the left
        chars = ""
        if line == "":
            return "..."

        if pos == 0:
            chars = "."
        else:
            chars = line[pos-1]

        # get the char at pos
        chars = chars + line[pos]

        # get the char to the right
        if pos >= len(line) - 1:
            chars = chars + "."
        else:
            chars = chars + line[pos+1]

        return chars

    def get_surrounding_chars(self, pos: int, line: str, above_line: str = "", below_line: str = ""):
        above_chars: str = self.get_relative_chars(above_line, pos)
        # in the below line, we need to look at: n, n-1, n+1
        below_chars = self.get_relative_chars(below_line, pos)

        # in the provided line, we need to look at n-1 and n+1
        # get the char to the left
        left_char = ""
        if pos == 0:
            left_char = "."
        else:
            left_char = line[pos-1]

        # get the char to the right
        right_char = ""
        if pos < len(line) - 1:
            right_char = line[pos+1]
        else:
            right_char = "."

        return above_chars, below_chars, left_char, right_char,

    def is_part_number(self, pos: int, line: str, above_line: str = "", below_line: str = "") -> bool:
        # in the above line, we need to look at: n, n-1, n+1
        above_chars, below_chars, left_char, right_char = self.get_surrounding_chars(pos, line, above_line, below_line)

        # combine all of the strings
        all_possible_symbols = above_chars + below_chars + left_char + right_char
        symbols = "#&*$%+-@/="
        for char in all_possible_symbols:
            if char.isdigit():
                continue
            if char == ".":
                continue
            if char not in symbols:
                continue
            return True
        return False

    def get_adjacent_numbers(self, line:str , pos: int) -> Tuple[int, int]:
        # walk forward to the end of the line, or the first non digit
        forward_index = pos
        backward_index = pos
        forward_nums = ""
        if pos < len(line) -1:
            forward_nums = line[pos+1:]

        backward_nums = ""
        if pos > 0:
            backward_nums = line[:pos]

        for i in range(len(forward_nums)):
            if not forward_nums[i].isdigit():
                break
            forward_index = forward_index + 1

        backward_nums = backward_nums[::-1]
        for i in range(len(backward_nums)):
            if not backward_nums[i].isdigit():
                break
            backward_index = backward_index - 1
        full_number_string = line[backward_index:forward_index+1]
        return int(full_number_string), forward_index

    def has_2_adjacent_numbers(self, pos: int, line: str, above_line: str, below_line: str):
        # in the above line, we need to look at: n, n-1, n+1
        above_chars, below_chars, left_char, right_char = self.get_surrounding_chars(pos, line, above_line, below_line)

        adjacent_numbers = 0
        if right_char.isdigit():
            adjacent_numbers = adjacent_numbers + 1
        if left_char.isdigit():
            adjacent_numbers = adjacent_numbers + 1

        prev_char = "."
        for char in above_chars:
            if char.isdigit() and not prev_char.isdigit():
                adjacent_numbers = adjacent_numbers + 1
            prev_char = char

        prev_char = "."
        for char in below_chars:
            if char.isdigit() and not prev_char.isdigit():
                adjacent_numbers = adjacent_numbers + 1
            prev_char = char

        if adjacent_numbers != 2:
            return False

        return True

    def get_gear_number(self, pos: int, line: str, above_line: str, below_line: str):
        above_chars, below_chars, left_char, right_char = self.get_surrounding_chars(pos, line, above_line, below_line)
        sum = 1
        i = 0
        while i < len(above_chars):
            char = above_chars[i]
            if not char.isdigit():
                i = i + 1
                continue
            number, index = self.get_adjacent_numbers(above_line, pos + (i-1))
            sum = sum * number
            i = index - pos + 2
        i = 0
        while i < len(below_chars):
            char = below_chars[i]
            if not char.isdigit():
                i = i + 1
                continue
            number, index = self.get_adjacent_numbers(below_line, pos + (i-1))
            sum = sum * number
            i = index - pos + 2
        if left_char.isdigit():
            number, index = self.get_adjacent_numbers(line, pos - 1)
            sum = sum * number
        if right_char.isdigit():
            number, index = self.get_adjacent_numbers(line, pos + 1)
            sum = sum * number
        return sum

    def process_input(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list = self.get_input_lines(file_path, file_name)
        sum = 0
        line_count = 0
        for i in range(len(lines)):
            above_line = ""
            line_count += 1
            if i >= 1:
                above_line = lines[i-1]

            target_line = lines[i]

            below_line = ""
            if i < len(lines) -1:
                below_line = lines[i+1]
            k = 0
            while k < len(target_line):
                if not target_line[k].isdigit():
                    k = k + 1
                    continue
                if not self.is_part_number(k, target_line, above_line, below_line):
                    k = k + 1
                    continue
                num, end_index = self.get_adjacent_numbers(target_line, k)
                sum = sum + num
                k = end_index + 1
        print(line_count)
        return sum

    def process_input2(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list = self.get_input_lines(file_path, file_name)
        sum = 0
        for i in range(len(lines)):
            target_line = lines[i]

            above_line = ""
            if i >= 1:
                above_line = lines[i-1]

            below_line = ""
            if i < len(lines) -1:
                below_line = lines[i+1]

            k = 0
            while k < len(target_line):
                if not target_line[k] == "*":
                    k = k + 1
                    continue
                if not self.has_2_adjacent_numbers(k, target_line, above_line, below_line):
                    k = k + 1
                    continue
                num = self.get_gear_number(k, target_line, above_line, below_line)
                sum = sum + num
                k = k + 1
        return sum
