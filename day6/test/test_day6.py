from collections.abc import Generator
from day6.day6 import DaySix
import pytest
import os

@pytest.fixture
def runner() -> Generator[DaySix]:
    runner = DaySix()
    yield runner

class TestDay6:
    def test_example_input_1(self, runner: DaySix):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name: str = "example_input.txt"
        res = runner.process_input(test_path, test_name)
        assert res == 288  # part 1

    def test_get_race_margin(self, runner: DaySix):
        race_time = 7
        race_distance = 9
        res = runner.get_race_margin(race_time, race_distance)
        assert res == 4


