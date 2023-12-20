#Advent of Code 2023 - Day 4
#Got part 1 to work but not part 2

from collections import defaultdict


file_name = 'd4_test_input.txt'

point_total = 0 

def return_points(common_elements):
    if len(common_elements) > 0: 
        return 2 ** (len(common_elements) - 1)
    else:
        return 0

with open(file_name, 'r') as file:

    num_lines = file.readlines()
    keys_range = len(num_lines)
    card_counts = dict.fromkeys(range(1, keys_range + 1), 1) 
    # card_counts[0] = 0
    card_counter = 1

    file.close()

with open(file_name, 'r') as file: 

    for line in file: 

        line = line.strip()

        card_split = line.split('|')

        winning_cards, game_cards = card_split[0], card_split[1]

        game_card_list_temp = game_cards.strip().split(" ")
        game_card_list = [int(card) for card in game_card_list_temp if card != '']

        winning_cards_list = winning_cards.split(":")
        winning_cards_list_temp = winning_cards_list[1]
        winning_cards_sep = winning_cards_list_temp.split(" ")
        winning_cards_list_final = [int(card) for card in winning_cards_sep if card.isdigit() and card != '']

        # card_sum = 0


        common_elements = [ele for ele in game_card_list if ele in winning_cards_list_final]
        for i in range(card_counter, card_counter + len(common_elements) + 1):
            card_counts[i] += 1 

        card_counter += 1
        # point_total += card_sum

# print(point_total)
print(sum(card_counts.values()))