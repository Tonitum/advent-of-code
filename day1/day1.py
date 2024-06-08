from utilities.loader import load_input

class DayOne:
    def get_input_lines(self, file_path, file_name) -> list:
        return load_input(file_path, file_name)

    def parse_line(self, line: str) -> int:
        """
        Find the first integer in a line and the last integer in a line, and
        add them together, returning the value
        """
        first_integer = self.find_first_integer(line)
        if first_integer == "none":
            return -1
        last_integer = self.find_last_integer(line)
        sum = first_integer + last_integer
        return int(sum)

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



