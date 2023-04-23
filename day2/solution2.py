#!/usr/bin/python3
import os

from aoc.utilities.parsing import load_input


# CONSTANTS
ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
DRAW = 3
WIN = 6

SHAPES = {
        # elf
        'A': ROCK,
        'B': PAPER,
        'C': SCISSORS,
        # player
        'X': ROCK,
        'Y': PAPER,
        'Z': SCISSORS
}

OUTCOMES = {
        'X': LOSE,
        'Y': DRAW,
        'Z': WIN
}

WINS = {
        'A': 'B',
        'B': 'C',
        'C': 'A',
}

LOSSES = {
        'A': 'C',
        'B': 'A',
        'C': 'B',
}

def parse_input(input_data: list) -> list:
    parsed_data = []
    elf_index = 0
    temp_list = []
    for line in input_data:
        line = line.strip("\n")
        moves = line.split(" ")

        parsed_data.append(moves)
    return parsed_data

def play_round_1(elf_move, player_move) -> int:
    ''' Play a round of Rock, Paper Scissors.
        Elf Move Reference Map:
            A: Rock
            B: Paper
            C: Scissors
        Player Move Reference Map:
            X: Rock 1
            Y: Paper 2
            Z: Scissors 3
    '''
    # get the elf move
    elf_score = SHAPES[elf_move]

    # get the player move
    player_score = SHAPES[player_move]

    # if the moves are the same, return a draw
    if elf_score == player_score:
        return (DRAW + player_score)

    # if not, calculate the winner
    if elf_score == ROCK and player_score == PAPER:
        return (WIN + player_score)
    if elf_score == PAPER and player_score == SCISSORS:
        return (WIN + player_score)
    if elf_score == SCISSORS and player_score == ROCK:
        return (WIN + player_score)

    return (LOSE + player_score)

def play_round_2(elf_move, outcome) -> int:
    ''' Play a round of Rock, Paper Scissors.
        Elf Move Reference Map:
            A: Rock
            B: Paper
            C: Scissors
        Player Move Reference Map:
            X: LOSE
            Y: DRAW
            Z: WIN
    '''
    outcome_score = OUTCOMES[outcome]
    player_move = ''

    if outcome_score == LOSE:
        player_move = LOSSES[elf_move]
    if outcome_score == DRAW:
        player_move = elf_move
    if outcome_score == WIN:
        player_move = WINS[elf_move]

    return outcome_score + SHAPES[player_move]



def main():
    tonitum = os.environ.get('TONITUM')
    input_path = os.path.abspath(f'{tonitum}/aoc/day2/input.txt')
    # input_path = os.path.abspath(f'{tonitum}/aoc/day2/test_input.txt')
    # input_path = os.path.abspath(f'{tonitum}/aoc/day2/test_input2.txt')

    data = load_input(input_path)
    parsed_data = parse_input(data)

    score_total = 0
    # print(len(parsed_data))
    for i in range(len(parsed_data)):
        score = play_round_1(parsed_data[i][0], parsed_data[i][1])
        score_total = score_total + score
    print(score_total)

    true_score = 0
    for i in range(len(parsed_data)):
        score = play_round_2(parsed_data[i][0], parsed_data[i][1])
        true_score = true_score + score
    print(true_score)



if __name__ == "__main__":
    main()
