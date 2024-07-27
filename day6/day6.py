from utilities.day import Day
import re


class DaySix(Day):
    def __init__(self) -> None:
        pass

    def get_race_margin(self, race_time: int, race_distance: int) -> int:
        return -1
    
    def build_races(self, race_times: str, race_distances: str) -> list[tuple[int, int]]:
        time_parts = race_times.split(":")
        times_string = time_parts[1]
        times = [int(time) for time in re.split("\s+", times_string)]
        distance_parts = race_distances.split(":")
        distances_string = distance_parts[1]
        distances = [int(distance) for distance in re.split("\s+", distances_string)]
        races: list[tuple[int,int]] = []
        for i in range(len(times)):
            races.append((times[i], distances[i]))
        return races

    def process_input(self, file_path: str, file_name: str) -> int:
        lines: list[str] = self.get_input_lines(file_path, file_name)
        return -1
