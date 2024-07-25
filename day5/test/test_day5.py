from day5.day5 import DayFive, ResourceLine, ResourceMap, part2
import os
import pytest
from collections.abc import Generator


@pytest.fixture
def runner() -> Generator[DayFive]:
    runner = DayFive()
    yield runner


class TestDay5:
    def test_example_file1(self, runner: DayFive):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name: str = "example_input.txt"
        res = runner.process_input_1(test_path, test_name)
        assert res == 35  # part 1
        # assert res == 46 # part 2

    def test_real_file1(self, runner: DayFive):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name: str = "real_input.txt"
        res = runner.process_input_1(test_path, test_name)
        assert res == 403695602  # part 1

    def test_get_seeds(self, runner: DayFive):
        seed_str = "seeds: 79 14 55 13"
        res = runner.get_seeds(seed_str)
        assert res == [79, 14, 55, 13]

    def test_build_map(self, runner: DayFive):
        map_lines = ["seed-to-soil map:", "50 98 2", "52 50 48", ""]
        map = runner.build_map(map_lines)
        assert map.name == "seed-to-soil"
        assert len(map.lines) == 2
        assert map.lines[0].destination_start == 50
        assert map.lines[0].destination_end == 52
        assert map.lines[0].source_start == 98
        assert map.lines[0].source_end == 100
        assert map.lines[1].destination_start == 52
        assert map.lines[1].destination_end == 100
        assert map.lines[1].source_start == 50
        assert map.lines[1].source_end == 98

        assert map.get_mapped_value(79) == 81
        assert map.get_mapped_value(14) == 14
        assert map.get_mapped_value(55) == 57
        assert map.get_mapped_value(13) == 13

    def test_build_maps(self, runner: DayFive):
        map_lines = ["seed-to-soil map:", "50 98 2", "52 50 48", ""]
        map_lines.extend(["soil-to-fertilizer map:", "0 15 37", "37 52 2", "39 0 15"])
        maps = runner.build_all_maps(map_lines)
        assert "seed-to-soil" in maps
        assert "soil-to-fertilizer" in maps

    def test_get_mapped_value(self, runner: DayFive):
        map_lines = ["seed-to-soil map:", "50 98 2", "52 50 48", ""]
        map_lines.extend(["soil-to-fertilizer map:", "0 15 37", "37 52 2", "39 0 15", ""])
        map_lines.extend(
            ["fertilizer-to-water map:", "49 53 8", "0 11 42", "42 0 7", "57 7 4", ""]
        )
        map_lines.extend(["water-to-light map:", "88 18 7", "18 25 70", ""])
        map_lines.extend(
            ["light-to-temperature map:", "45 77 23", "81 45 19", "68 64 13", ""]
        )
        map_lines.extend(["temperature-to-humidity map:", "0 69 1", "1 0 69", ""])
        map_lines.extend(["humidity-to-location map:", "60 56 37", "56 93 4"])
        maps = runner.build_all_maps(map_lines)
        res = runner.filter_seed_through_maps(79, maps)
        assert res == 82
        res = runner.filter_seed_through_maps(14, maps)
        assert res == 43
        res = runner.filter_seed_through_maps(55, maps)
        assert res == 86
        res = runner.filter_seed_through_maps(13, maps)
        assert res == 35

    def test_example_file2(self, runner: DayFive):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name: str = "example_input.txt"
        puzzle_input = ""
        with open(test_path + "/" + test_name) as f:
            puzzle_input = f.read()
        res = part2(puzzle_input)
        assert res == 46  # part 2

    def test_real_file2(self, runner: DayFive):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name: str = "real_input.txt"
        puzzle_input = ""
        with open(test_path + "/" + test_name) as f:
            puzzle_input = f.read()
        res = part2(puzzle_input)
        assert res == 46  # part 2


class TestResourceMap:
    def test_get_mapped_value_no_lines(self):
        mapper = ResourceMap("")
        res = mapper.get_mapped_value(1)
        assert res == 1

    def test_get_mapped_value_in_lines(self):
        mapper = ResourceMap("")
        lines = [ResourceLine(10, 5, 2), ResourceLine(20, 10, 2)]
        mapper.lines = lines
        res = mapper.get_mapped_value(6)
        assert res != 1
        assert res == 11

    def test_get_mapped_value_not_in_lines(self):
        mapper = ResourceMap("")
        lines = [ResourceLine(10, 5, 2), ResourceLine(20, 10, 2)]
        mapper.lines = lines
        res = mapper.get_mapped_value(1)
        assert res == 1
