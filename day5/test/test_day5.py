from day5.day5 import DayFive
import os
import pytest

@pytest.fixture
def runner():
    runner = DayFive()
    yield runner

class TestDay4:
    def test_example_file1(self, runner):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "example_input.txt"
        res = runner.process_input(test_path, test_name)
        assert res == 35 # part 1

    def test_get_seeds(self, runner):
        seeds_input = "seeds: 79 14 55 13"
        res = runner.get_seeds(seeds_input)
        assert res == ["79","14","55","13"]

    def test_get_a_to_b_names(self, runner):
        line = "seed-to-soil map:"
        res_a, res_b = runner.get_a_b_names(line)
        assert res_a == "seed"
        assert res_b == "soil"

    def test_get_a_to_b_names_malformed(self, runner):
        line = "seed-to-soilmap:"
        with pytest.raises(ValueError):
            _ = runner.get_a_b_names(line)

    def test_get_a_to_b_names_invalid(self, runner):
        line = "seed-soil map:"
        with pytest.raises(ValueError):
            _ = runner.get_a_b_names(line)

    def test_process_map_range(self, runner):
        map_line1 = "50 98 2"
        map_line2 = "52 50 48"
        seed1 = "79"
        soil1 = "81"
        seed2 = "14"
        soil2 = "14"
        seed3 = "55"
        soil3 = "57"
        seed4 = "13"
        soil4 = "13"

        seed_to_soil_map: dict = runner.get_a_to_b_mapping()


