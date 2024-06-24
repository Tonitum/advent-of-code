from utilities.day import Day

class DayOne(Day):
    def parse_line(self, line: str) -> int:
        """
        Find the first integer in a line and the last integer in a line, and
        add them together, returning the value
        """
        first_integer_digit = self.find_first_integer(line)
        first_integer_digit_index = line.find(first_integer_digit)
        first_spelled_integer, first_spelled_index_index = self.find_first_spelled_integer(line)

        if first_integer_digit == "none" and first_spelled_integer == "none":
            # if both of these are none, there are no digits in this line
            return -1

        first_number = "none"
        if first_spelled_integer != "none":
            if first_integer_digit_index == -1 or first_integer_digit_index > first_spelled_index_index:
                first_number = first_spelled_integer
            else:
                first_number = first_integer_digit
        else:
            first_number = first_integer_digit

        last_number = "none"
        last_digit_number = self.find_last_integer(line)
        last_digit_number_index = line.rfind(last_digit_number)
        last_spelled_number, last_spelled_number_index = self.find_last_spelled_integer(line)
        if last_spelled_number != "none":
            if last_digit_number_index == -1 or last_digit_number_index < last_spelled_number_index:
                last_number = last_spelled_number
            else:
                last_number = last_digit_number
        else:
            last_number = last_digit_number

        sum = first_number + last_number

        return int(sum)

    def find_spelled_digit(self, digit_string: str, line: str, first: bool = True) -> int:
        index = -1
        possible_index = -1
        if first:
            possible_index = line.find(digit_string)
        else:
            possible_index = line.rfind(digit_string)
        if possible_index != -1:
            index = possible_index
        return index

    def find_spelled_integer_locations(self, line: str, first: bool = True) -> dict:
        digits = {}
        digits["1"] = self.find_spelled_digit("one", line, first)
        digits["2"] = self.find_spelled_digit("two", line, first)
        digits["3"] = self.find_spelled_digit("three", line, first)
        digits["4"] = self.find_spelled_digit("four", line, first)
        digits["5"] = self.find_spelled_digit("five", line, first)
        digits["6"] = self.find_spelled_digit("six", line, first)
        digits["7"] = self.find_spelled_digit("seven", line, first)
        digits["8"] = self.find_spelled_digit("eight", line, first)
        digits["9"] = self.find_spelled_digit("nine", line, first)
        return digits

    def find_first_spelled_integer(self, line: str):
        digits = self.find_spelled_integer_locations(line)

        index = -1
        char = "none"
        for k, v in digits.items():
            if v == -1:
                continue
            if index == -1:
                index = v
                char = k
                continue
            if index > v:
                index = v
                char = k
        return char, index

    def find_last_spelled_integer(self, line: str):
        digits = self.find_spelled_integer_locations(line, False)

        index = -1
        char = "none"
        for k, v in digits.items():
            if v == -1:
                continue
            if index == -1:
                index = v
                char = k
                continue
            if index < v:
                index = v
                char = k
        return char, index

    def find_first_integer(self, line: str) -> str:
        """
        Find the first integer in a line and return it. If no integer is found,
        return -1.
        """
        for char in line:
            if char.isdigit():
                return char
        return "none"

    def find_last_integer(self, line: str) -> str:
        """
        Find the first integer in a line and return it. If no integer is found,
        return -1.
        """
        return self.find_first_integer(line[::-1])

    def process_input(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines = self.get_input_lines(file_path, file_name)
        total_sum = 0
        for line in lines:
            line_sum = self.parse_line(line)
            if line_sum == -1:
                break
            total_sum = total_sum + line_sum
        return total_sum
