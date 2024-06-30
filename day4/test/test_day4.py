import os
from day4.day4 import DayFour

class TestDay4:
    def test_example_file1(self):
        runner = DayFour()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "example_input.txt"
        res = runner.process_input(test_path, test_name)
        assert res == 13 # part 1

    def test_example_file2(self):
        runner = DayFour()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "example_input.txt"
        res = runner.process_input2(test_path, test_name)
        assert res == 30 # part 1

    def test_get_card_winnings(self):
        runner = DayFour()
        card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        res = runner.get_card_winnings(card)
        assert res == [2,3,4,5] # part 1

    def test_real_file(self):
        runner = DayFour()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "real_input.txt"
        res = runner.process_input(test_path, test_name)
        assert res < 108326 # part 1
        assert res == 18653 # part 1
        res = runner.process_input2(test_path, test_name)
        assert res == 18653 # part 1

