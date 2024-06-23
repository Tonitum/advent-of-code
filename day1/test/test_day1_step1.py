import os
from day1.day1 import DayOne

class TestDay1Step1:
    def test_get_input_lines(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input_example.txt"
        handler = DayOne()
        lines = handler.get_input_lines(test_path, test_name)
        assert lines != []

    def test_find_first_integer(self):
        handler = DayOne()
        res = handler.find_first_integer("1asdf4")
        assert res == "1"
        res = handler.find_first_integer("as2d3f")
        assert res == "2"
        res = handler.find_first_integer("asdf1")
        assert res == "1"
        res = handler.find_first_integer("asdf")
        assert res == "none"

    def test_find_last_integer(self):
        handler = DayOne()
        res = handler.find_last_integer("1asdf4")
        assert res == "4"
        res = handler.find_last_integer("1asd3f")
        assert res == "3"
        res = handler.find_last_integer("1asdf")
        assert res == "1"

    def test_parse_line(self):
        handler = DayOne()
        line = "dqfournine5four2jmlqcgv"
        res = handler.parse_line(line)
        assert res ==42
        line = "7ggzdnjxndfive"
        res = handler.parse_line(line)
        assert res == 75
        line = "twofive4threenine"
        res = handler.parse_line(line)
        assert res == 29
        line = "dttwonezbgmcseven5seven"
        res = handler.parse_line(line)
        assert res == 27
        line = "ggrbl5cthnzlsbjssixpt"
        res = handler.parse_line(line)
        assert res ==56 

    def test_find_first_spelled_integer_no_spelled_number(self):
        handler = DayOne()
        line = "12359291"
        res, index = handler.find_first_spelled_integer(line)
        assert res == "none"

    def test_find_first_spelled_integer_nominal(self):
        handler = DayOne()
        line = "two1nine"
        res, index = handler.find_first_spelled_integer(line)
        assert res == "2"
        assert index == 0

    def test_find_first_spelled_integer_overlap(self):
        handler = DayOne()
        line = "eightwothree"
        res, index = handler.find_first_spelled_integer(line)
        assert res == "8"
        assert index == 0

    def test_find_last_spelled_integer_nominal(self):
        handler = DayOne()
        line = "eightwothree"
        res, index = handler.find_last_spelled_integer(line)
        assert res == "3"
        assert index == 7

    def test_find_last_spelled_integer_none(self):
        handler = DayOne()
        line = "nane"
        res, index = handler.find_last_spelled_integer(line)
        assert res == "none"
        assert index == -1

    def test_process_input_example(self):
        handler = DayOne()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input_example.txt"
        res = handler.process_input(test_path, test_name)
        assert res == 142

    def test_process_example_input_step_2(self):
        handler = DayOne()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input_example_2.txt"
        res = handler.process_input(test_path, test_name)
        assert res == 281

    def test_process_input(self):
        handler = DayOne()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "real_input.txt"
        res = handler.process_input(test_path, test_name)
        assert res == 54087
