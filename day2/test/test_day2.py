import os
from day2.day2 import DayTwo

class TestDay2:
    def test_example_games(self):
        runner = DayTwo()
        game1_string = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game2_string = "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        game3_string = "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        game4_string = "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        game5_string = "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        assert runner.is_game_possible(game1_string)
        assert runner.is_game_possible(game2_string)
        assert not runner.is_game_possible(game3_string)
        assert not runner.is_game_possible(game4_string)
        assert runner.is_game_possible(game5_string)

    def test_example_file(self):
        runner = DayTwo()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "test_input_1.txt"
        res = runner.process_input(test_path, test_name)
        # assert res == 8 # part 1
        assert res == 2286 # part 2

    def test_real_games(self):
        runner = DayTwo()
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_name = "real_input.txt"
        res = runner.process_input(test_path, test_name)
        # assert res == 2237 # part 1
        assert res == 66681 # part 2

    def test_example_games_part_2(self):
        runner = DayTwo()
        game1_string = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game2_string = "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
        game3_string = "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
        game4_string = "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        game5_string = "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        assert runner.get_game_power(game1_string) == 48
        assert runner.get_game_power(game2_string) == 12
        assert runner.get_game_power(game3_string) == 1560
        assert runner.get_game_power(game4_string) == 630
        assert runner.get_game_power(game5_string) == 36
