import os
from day1.day1 import DayOne

class TestDay1Step1:
    def test_get_input_lines(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input1.txt"
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
        line = "1asdf2"
        res = handler.parse_line(line)
        assert res == 12
        line = "1as93fh"
        res = handler.parse_line(line)
        assert res == 13
        line = "asfh"
        res = handler.parse_line(line)
        assert res == -1

    def test_process_input_example(self):
        handler = DayOne()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input1.txt"
        res = handler.process_input(test_path, test_name)
        assert res == 142

    def test_process_input_step_1(self):
        handler = DayOne()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input2.txt"
        res = handler.process_input(test_path, test_name)
        assert res == 54708





