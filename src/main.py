"""
Created by Daechathon and Jules on 6/1/2022
A game of rock paper scissors against a markov chain AI
"""
import random
from logging import exception

# x beats y
legal_moves = ['rock', 'paper', 'scissors']
winning_move_list = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
move_index_map = {'rock': 0, 'paper': 1, 'scissors': 2, 0: 'rock', 1: 'paper', 2: 'scissors'}

# 3 x 3 matrix of move transitions
# see move_index_map for indices of moves
markov_matrix = []


# cheaty black magic
# returns a valid move
def markov_move(current_move):  # TODO implement markov chain
    return 'not implemented yet'


# returns the move that beats the most popular move transition
def best_markov_move(current_move):
    if current_move == '':
        current_move = move_index_map[random.randint(0, 2)]

    if current_move not in legal_moves:
        raise ValueError('illegal move')
    if len(markov_matrix) != 3 or len(markov_matrix[0]) != 3:
        raise ValueError('markov_matrix not initialized')

    idx = move_index_map[current_move]
    return winning_move_list[move_index_map[markov_matrix[idx].index(max(markov_matrix[idx]))]]


# updates the markov matrix
def update_markov(current_move, previous_move):
    if current_move not in legal_moves or previous_move not in legal_moves:
        raise ValueError('illegal move')

    # checks if the markov list is not the length of 3 then raises an exception
    if len(markov_matrix) != 3 or len(markov_matrix[0]) != 3:
        raise ValueError('markov_matrix not initialized')

    # increments index matching the move transition
    markov_matrix[move_index_map[current_move]][move_index_map[previous_move]] += 1


# initializes markov matrix with zero values
def init_markov():
    global markov_matrix
    markov_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# return 0 for tie, 1 for player 1, 2 for player 2
def move(player1_move, player2_move):
    if player1_move not in legal_moves or player2_move not in legal_moves:
        raise ValueError('illegal move')

    if player1_move == player2_move:
        return 0
    if winning_move_list[player1_move] == player2_move:
        return 2
    if winning_move_list[player2_move] == player1_move:
        return 1


def start_game():

    player_score = 0
    markov_score = 0
    previous_move = ''
    init_markov()

    while 1:
        print(f'Player: {player_score} Markov: {markov_score}')
        print('Please enter rock, paper, scissors, or stop if you wish to quit')
        input_string = input().lower()

        if input_string == 'stop':
            break
        if input_string != 'rock' and input_string != 'paper' and input_string != 'scissors':
            continue

        markov_turn = best_markov_move(previous_move)
        print(f'Markov plays {markov_turn}')
        turn_outcome = move(input_string, markov_turn)
        if previous_move != '':
            update_markov(input_string, previous_move)
        previous_move = input_string

        if turn_outcome == 1:
            player_score += 1
        elif turn_outcome == 2:
            markov_score += 1

    return player_score, markov_score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    score = start_game()
    print(f'Final Score: {score[0]} - {score[1]}')
