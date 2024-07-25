from utilities.day import Day
import re


class ResourceLine:
    def __init__(
        self, destination_range_start: int, source_range_start: int, range_length: int
    ) -> None:
        self.source_start: int = source_range_start
        self.source_end: int = source_range_start + range_length
        self.destination_start: int = destination_range_start
        self.destination_end: int = destination_range_start + range_length


class ResourceMap:
    def __init__(self, name: str) -> None:
        self.lines: list[ResourceLine] = []
        self.name = name

    def add_map_line(
        self, destination_start: int, source_start: int, range_length: int
    ) -> None:
        new_line = ResourceLine(destination_start, source_start, range_length)
        self.lines.append(new_line)

    def get_mapped_value(self, source_key: int) -> int:
        destination_value: int = -1
        for resource_line in self.lines:
            if source_key in range(
                resource_line.source_start, resource_line.source_end
            ):
                delta: int = source_key - resource_line.source_start
                destination_value = resource_line.destination_start + delta

        if destination_value == -1:
            # if the supplied key was not in any of the source ranges, then it maps to the same destination value
            return source_key

        return destination_value


class Interval:
    def __init__(self, start: int, length: int) -> None:
        self.start = start
        self.length = length
        self.end = start + length

def part2(puzzle_input):
    segments = puzzle_input.split('\n\n')
    intervals = []

    for seed in re.findall(r'(\d+) (\d+)', segments[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        intervals.append((x1, x2, 1))

    min_location = float('inf')
    while intervals:
        x1, x2, level = intervals.pop()
        if level == 8:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', segments[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:    # no overlap
                continue
            if x1 < y1:                 # split original interval at y1
                intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:                 # split original interval at y2
                intervals.append((y2, x2, level))
                x2 = y2
            intervals.append((x1 + diff, x2 + diff, level + 1)) # perfect overlap -> make conversion and let pass to next nevel 
            break

        else:
            intervals.append((x1, x2, level + 1))
  
    return min_location

class DayFive(Day):
    def get_seed_intervals(self, seed_string: str) -> list[Interval]:
        seed_numbers = self.get_seeds(seed_string)
        seed_intervals: list[Interval] = []
        for i in range(len(seed_numbers)):
            range_start = seed_numbers[i * 2]
            range_length = seed_numbers[(i * 2) + 1]
            interval = Interval(range_start, range_length)
            seed_intervals.append(interval)
        return seed_intervals

    def get_seeds(self, seed_string: str) -> list[int]:
        line_parts: list[str] = seed_string.split(":")
        seeds: list[str] = line_parts[1].strip().split(" ")
        seed_numbers: list[int] = [int(seed) for seed in seeds]
        return seed_numbers

    def get_map_name(self, line: str) -> str:
        return line.split(" ")[0]

    def parse_map_line(self, line: str) -> list[int]:
        parts = line.split(" ")
        dest_start = int(parts[0])
        source_start = int(parts[1])
        length = int(parts[2])
        return [dest_start, source_start, length]

    def build_map(self, lines: list[str]) -> ResourceMap:
        name = self.get_map_name(lines.pop(0))
        map = ResourceMap(name)
        for line in lines:
            if line == "":
                continue
            parts = self.parse_map_line(line)
            map.add_map_line(parts[0], parts[1], parts[2])

        return map

    def build_all_maps(self, lines: list[str]) -> dict[str, ResourceMap]:
        maps: dict[str, ResourceMap] = {}
        slice_start: int = 0
        for i in range(0, lines.count("")):
            slice_end: int = lines.index("", slice_start)
            map_lines = lines[slice_start:slice_end]
            current_map: ResourceMap = self.build_map(map_lines)
            maps[current_map.name] = current_map
            slice_start = slice_end + 1

        map_lines = lines[slice_start:]
        current_map = self.build_map(map_lines)
        maps[current_map.name] = current_map

        return maps

    def filter_seed_through_maps(self, seed: int, maps: dict[str, ResourceMap]) -> int:
        mapped_value = seed
        for map in maps.values():
            mapped_value = map.get_mapped_value(mapped_value)
        return mapped_value

    def process_input_1(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list[str] = self.get_input_lines(file_path, file_name)
        seeds = self.get_seeds(lines.pop(0))
        _ = lines.pop(0)
        maps = self.build_all_maps(lines)
        locations: list[int] = []
        for seed in seeds:
            locations.append(self.filter_seed_through_maps(seed, maps))

        locations.sort()
        return locations[0]

    def process_input(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list[str] = self.get_input_lines(file_path, file_name)
        _ = lines.pop(0)
        return -1
