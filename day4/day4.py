from utilities.day import Day
from typing import Tuple
import sys

class DayFour(Day):
    def trim_card_number(self, card: str) -> Tuple[str, str]:
        card_parts =card.split(":")
        card_id = card_parts[0].strip()
        trimmed_card = card_parts[1].strip()
        return trimmed_card, card_id

    def get_part_numbers(self, card_left_block: str):
        card_left_block = card_left_block.strip()
        winning_numbers = card_left_block.split(" ")
        while winning_numbers.count("") > 0:
            winning_numbers.remove("")
        
        return winning_numbers

    def get_card_points(self, card: str):
        trimmed_card, _ = self.trim_card_number(card)
        # get the left and right card halves
        card_parts = trimmed_card.split("|")
        left_part = card_parts[0].strip()
        right_part = card_parts[1].strip()
        winning_numbers = self.get_part_numbers(left_part)
        candidate_numbers = self.get_part_numbers(right_part)

        points = 0
        for number in candidate_numbers:
            if number not in winning_numbers:
                continue
            if points == 0:
                points = 1
                continue
            points = points * 2

        return points

    def get_card_winnings(self, card: str):
        trimmed_card, card_id_part = self.trim_card_number(card)
        card_id = int(card_id_part.split(" ")[-1])

        # get the left and right card halves
        card_parts = trimmed_card.split("|")
        left_part = card_parts[0].strip()
        right_part = card_parts[1].strip()
        winning_numbers = self.get_part_numbers(left_part)
        candidate_numbers = self.get_part_numbers(right_part)
        won_cards_count = 0
        for number in candidate_numbers:
            if number not in winning_numbers:
                continue
            won_cards_count = won_cards_count + 1
        won_cards = [i for i in range(card_id+1, card_id + won_cards_count + 1)]
        return won_cards

    def get_all_cards(self, cards: list, reference: dict) -> list:
        base_cards = cards
        won_card_ids = []
        for card in base_cards:
            won_card_ids.extend(self.get_card_winnings(card))

        won_cards = []
        for card_id in won_card_ids:
            won_cards.append(reference[str(card_id)])

        if len(won_cards) > 0:
            won_cards.extend(self.get_all_cards(won_cards, reference))
        # won_cards.append(base_card)
        return won_cards

    def process_input(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list = self.get_input_lines(file_path, file_name)
        sum = 0
        for card in lines:
            points = self.get_card_points(card)
            sum = sum + points
        return sum

    def process_input2(self, file_path: str, file_name: str) -> int:
        file_path = file_path
        file_name = file_name
        lines: list = self.get_input_lines(file_path, file_name)
        card_reference = {}
        for line in lines:
            parts = line.split(":")
            card_reference[parts[0].split(" ")[-1]] = line
        # print(sys.getrecursionlimit())
        # sys.setrecursionlimit(2000)

        total_cards = []
        total_cards.extend(lines)
        total_cards.extend(self.get_all_cards(lines, card_reference))
        total_cards.sort()
        return len(total_cards)
