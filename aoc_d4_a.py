#Advent of Code 2023 - Day 4

file_name = 'd4_input.txt'

point_total = 0 

with open(file_name, 'r') as file:

    for line in file: 
        # line = file.readline()
        line = line.strip()

        card_split = line.split('|')

        winning_cards, game_cards = card_split[0], card_split[1]

        game_card_list_temp = game_cards.strip().split(" ")
        game_card_list = [int(card) for card in game_card_list_temp if card != '']

        winning_cards_list = winning_cards.split(":")
        winning_cards_list_temp = winning_cards_list[1]
        winning_cards_sep = winning_cards_list_temp.split(" ")
        # print(winning_cards_sep)
        winning_cards_list_final = [int(card) for card in winning_cards_sep if card.isdigit() and card != '']

        card_sum = 0
        common_elements = [ele for ele in game_card_list if ele in winning_cards_list_final]
        if len(common_elements) > 0: 
            card_sum = 2 ** (len(common_elements) - 1)
        else:
            card_sum = 0
        
        point_total += card_sum

print(point_total)