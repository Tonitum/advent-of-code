from utilities.day import Day

class DayFive(Day):
    def get_seeds(self, seed_line: str) -> list[str]:
        parts = seed_line.split(":")
        if len(parts) != 2:
            raise ValueError("Seed line was malformed")

        name = parts[0].strip()
        if name != "seeds":
            raise ValueError("Line provided was not a seed line")
        seed_strings = parts[1].strip().split(" ")
        return seed_strings

    def get_a_b_names(self, a_to_b_line: str) -> tuple[str, str]:
        line_parts = a_to_b_line.split(" ") 
        if len(line_parts) != 2:
            raise ValueError
        ab_parts = line_parts[0].split("-")
        if len(ab_parts) != 3:
            raise ValueError
        a_name = ab_parts[0]
        b_name = ab_parts[2]
        return a_name, b_name

    def process_map_range(self, line: str, a: str, b: str):
        line_parts = line.split(" ")
        if len(line_parts) != 3:
            raise ValueError
        destination_range_start = int(line_parts[0])
        source_range_start = int(line_parts[1])
        range_length = int(line_parts[2])
        mapped_source_indices = [ i for i in range(source_range_start, source_range_start + range_length) ]
        mapped_destination_indices = [ i for i in range(destination_range_start, destination_range_start + range_length) ]

        a_to_b_map: {}
        for mapping in mapped_source_indices:
            pass

    def process_a_to_b_map(self, lines: list[str]):
        a_name: str
        b_name: str
        a_name, b_name = self.get_a_b_names(lines[0])

    def get_a_to_b_mapping(self, map_lines) -> dict[str, int]:
        return {}

    def process_input(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list = self.get_input_lines(file_path, file_name)
        sum = 0
        return sum

