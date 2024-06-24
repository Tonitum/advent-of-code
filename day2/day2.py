from utilities.day import Day

class DayTwo(Day):
    MAX_COUNTS = {}
    MAX_COUNTS["red"] = 12
    MAX_COUNTS["green"] = 13
    MAX_COUNTS["blue"] = 14

    def is_round_possible(self, round_string: str) -> bool:
        color_counts = round_string.strip().split(",")
        for color_round in color_counts:
            color_parts = color_round.strip().split(" ")
            color_count = color_parts[0]
            color_name = color_parts[1]
            if int(color_count) <= self.MAX_COUNTS[color_name]:
                continue
            return False
        return True

    def is_game_possible(self, game_string: str) -> bool:
        split_rounds = game_string.split(";")
        # parse through each round, determining if the round was possible
        possible = True
        for round_string in split_rounds:
            possible = self.is_round_possible(round_string)
            if not possible:
                break

        return possible

    def get_game_power(self, game_string: str) -> int:
        # split the game into rounds
        split_rounds = game_string.split(";")
        # determine the largest count for each color
        red_max: int = -1
        green_max: int = -1
        blue_max: int = -1
        for game_round in split_rounds:
            game_round = game_round.strip()
            # split the game round by colors
            round_colors = game_round.split(",")
            for color in round_colors:
                parts = color.strip().split(" ")
                count = parts[0]
                color_name = parts[1]
                if color_name == "blue":
                    if blue_max <= int(count):
                        blue_max = int(count)
                if color_name == "red":
                    if red_max <= int(count):
                        red_max = int(count)
                if color_name == "green":
                    if green_max <= int(count):
                        green_max = int(count)
        # multiple the largest of each color together
        game_power: int = red_max * blue_max * green_max
        return game_power

    def get_game_id(self, game_string: str) -> str:
        parts = game_string.split(":")
        id_parts = parts[0].split(" ")
        game_id = id_parts[1]
        return game_id

    def process_input(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines = self.get_input_lines(file_path, file_name)

        game_results = {}
        for line in lines:
            game_id = self.get_game_id(line)
            game_possible = self.get_game_power(line.split(":")[1].strip())
            game_results[game_id] = game_possible

        total_sum = 0
        for game_id, result in game_results.items():
            total_sum = total_sum + int(result)
        return total_sum
