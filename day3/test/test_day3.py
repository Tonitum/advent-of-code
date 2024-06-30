import os
from day3.day3 import DayThree

class TestDay3:
    def test_example_games(self):
        runner = DayThree()
        lines = [
            "..*.......",
            "467..114..",
            "...*......",
            "..35..633."
        ]
        res = runner.is_part_number(2, lines[1], lines[0], lines[2])
        assert res
        res = runner.is_part_number(1, lines[1], lines[0], lines[2])
        assert res
        res = runner.is_part_number(0, lines[1], lines[0], lines[2])
        assert not res
        res = runner.is_part_number(5, lines[1], lines[0], lines[2])
        assert not res

    def test_get_adjacent_nums(self):
        runner = DayThree()
        line = "467..114.."
        pos = 1
        res, index = runner.get_adjacent_numbers(line, pos)
        assert res == 467
        assert index == 2
        pos = 6
        res, index = runner.get_adjacent_numbers(line, pos)
        assert res == 114
        assert index == 7
        line = "467..1.1.1"
        res, index = runner.get_adjacent_numbers(line, 7)
        assert res == 1
        assert index == 7
        line = ".1234.678"
        res, index = runner.get_adjacent_numbers(line, 3)
        assert res == 1234
        assert index == 4

    def test_example_file1(self):
        runner = DayThree()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "example_input_1.txt"
        res = runner.process_input(test_path, test_name)
        assert res == 4361 # part 1

    def test_broken_case(self):
        above_line  = '....758..........................*......=.............@................................273......911...#....@666...+193......................'
        line        = ".............604....483..&144.859......807...-.........995..-218.770............37.512.*.........*.........................215...........117"
        below_line  = '......354..........*...............$........849.*.................................*.....242....469.&764.........................959*128.$...'
        runner = DayThree()
        res = runner.is_part_number(139, line, above_line, below_line)
        assert not res

    def test_has_2_adjacent_numbers(self):
        lines = [
            "467..114..",
            "...*.....*",
            "..35..633."]
        pos = 3
        runner = DayThree()
        res = runner.has_2_adjacent_numbers(pos, lines[1], lines[0], lines[2])
        assert res

    def test_has_2_adjacent_numbers2(self):
        lines = [
            ".1.",
            "*..",
            ".1."]
        pos = 0
        runner = DayThree()
        res = runner.has_2_adjacent_numbers(pos, lines[1], lines[0], lines[2])
        assert res

    def test_get_gear_number5(self):
        lines = [
            ".10.......",
            "...*......",
            "....10...."]
        pos = 3
        runner = DayThree()
        res = runner.get_gear_number(pos, lines[1], lines[0], lines[2])
        assert res == 100

    def test_example_file(self):
        runner = DayThree()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "example_input_1.txt"
        res = runner.process_input2(test_path, test_name)
        assert res == 467835 # part 1

    def test_real_file(self):
        runner = DayThree()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "real_input.txt"
        res = runner.process_input(test_path, test_name)
        assert res == 527446 # part 1
        res = runner.process_input2(test_path, test_name)
        assert res == 73201705 # part 2
