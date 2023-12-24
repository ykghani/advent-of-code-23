#AOC 2023 Day 7 - Camel Poker
'''Rank all of the given hands based on their strength and multiply by bid points to get total score'''

from collections import namedtuple
import bisect 

Hand = namedtuple('Hand', ['cards', 'bid'])

card_scores = {'2': 2,
               '3': 3,
               '4': 4,
               '5': 5, 
               '6': 6,
               '7': 7,
               '8': 8,
               '9': 9,
               'T': 10,
            #    'J': 11, updated for part 1 - J is worth 1 point 
               'Q': 12,
               'K': 13,
               'A': 14,
               'J': 1 }

hand_scores = {'high_card': 1,
               'one_pair': 2,
               'two_pair': 3,
               'three_kind': 4,
               'full_house': 5,
               'four_kind': 6,
               'five_kind': 7}

game = []

file_path = 'aoc_d7_input.txt'

def convert_cards(card_str):
    output_list = []

    for i in range(len(card_str)):
        card_val = int(card_scores.get(card_str[i]))
        output_list.append(card_val)

    return output_list

with open(file_path, 'r') as file:

    for line in file:
        line = line.strip().split()
        card_list = convert_cards(line[0])
        hand = Hand(cards = card_list, bid = int(line[1]))
        game.append(hand)
    
file.close()

def get_max_count(cards):
    max_count = 1
    card_set = set(cards)

    for card in card_set:
        # card_sum = len([i for i in cards if i == card])
        card_sum = cards.count(card)

        if card_sum > max_count:
            max_count = card_sum
    
    return max_count


def check_hand(hand):
    cards = hand.cards
    uniq_cards = set(cards)
    num_uniq_cards = len(uniq_cards)
    hand_type = ''

    if num_uniq_cards == 1:
        hand_type = 'five_kind'

    elif num_uniq_cards == 2: #Two options: either 4 of a kind or full house 

        max_count = get_max_count(cards)

        if max_count == 4:
            hand_type = 'four_kind'
        else:
            hand_type = 'full_house'
    
    elif num_uniq_cards == 3: #Two options: either 3 of a kind or two pair
        
        max_count = get_max_count(cards)

        if max_count == 3:
            hand_type = 'three_kind'
        else:
            hand_type = 'two_pair' 
    
    elif num_uniq_cards == 4:
        hand_type = 'one_pair'
    
    else: #len(set(cards)) == 5
        hand_type = 'high_card'
    
    return hand_type

#Requires that input hand has at least 1 joken in it 
def check_hand_joker(hand):
    cards = hand.cards
    joker_count = cards.count(1) #int, number of jokers
    uniq_cards = set(cards) #set of unique cards
    uniq_cards_no_joke = uniq_cards - {1} #set of unique cards withoutjoker
    num_uniq_cards = len(uniq_cards) #int, number of unique cards (inc. joker)
    num_uniq_cards_no_joke = len(uniq_cards_no_joke) #int, number of unique cards without joker 
    card_list_no_joke = [card for card in cards if card != 1]
    hand_type = ''

    if joker_count == 5:
        hand_type = 'five_kind'

    elif joker_count == 4:
        hand_type = 'five_kind'
    
    elif joker_count == 3:
        if num_uniq_cards_no_joke == 1:
            hand_type = 'five_kind'
        
        else:
            hand_type = 'four_kind'
    
    elif joker_count == 2: #IF THERE'S AN ERROR IT'S HERE - SOMETHING TO DO WITH FULL HOUSES 
        if num_uniq_cards_no_joke == 3:
            hand_type = 'three_kind'
        
        elif num_uniq_cards_no_joke == 2:
            max_cards = 0
            
            for card in card_list_no_joke:
                card_count = card_list_no_joke.count(card)
                if card_count > max_cards:
                    max_cards = card_count
            
            if max_cards == 2:
                hand_type = 'four_kind'
            else:
                hand_type = 'three_kind'

        else:
            hand_type = 'five_kind'
    
    else: #Case where there is only 1 joker
        if num_uniq_cards_no_joke == 4:
            hand_type = 'one_pair'
        
        elif num_uniq_cards_no_joke == 3: #three unique cards, 1 joker, means 1 card repeated
            hand_type = 'three_kind'

        elif num_uniq_cards_no_joke == 2: #Two pairs + 1 Joker OR 3 of a kind, 1 card, and 1 joker
            
            max_cards = 0

            for card in uniq_cards_no_joke:
                card_count = card_list_no_joke.count(card)
                if card_count > max_cards:
                    max_cards = card_count
            
            if max_cards == 3:
                hand_type = 'four_kind'
            
            else:
                hand_type = 'full_house'
                    
        else: #Num uniq cards no joke == 1, all 4 cards are the same 
            hand_type = 'five_kind'
    
    return hand_type



def pairwise_key(hand):
    # scored_hand = [card_scores[i] for i in hand]
    cards = hand.cards
    scored_hand = [card_scores.get(i) for i in cards]
    scored_tuple = tuple(scored_hand)
    # return tuple(scored_hand)
    return scored_hand


high_card, one_pair, two_pair, full_house, three_kind, four_kind, five_kind = [], [], [], [], [], [], []


for hand in game:
    # cards = [card_scores.get(card) for card in hand.cards]
    cards = hand.cards
    if 1 in cards:
        hand_score = check_hand_joker(hand)
    else:
        hand_score = check_hand(hand)

    if hand_score == 'five_kind':
        # index_to_insert = bisect.bisect_left(five_kind, cards, key= pairwise_key)
        # five_kind.insert(index_to_insert, hand)
        five_kind.append(hand)
    
    elif hand_score == 'four_kind':
        # index_to_insert = bisect.bisect_left(four_kind, cards, key= pairwise_key)
        # four_kind.insert(index_to_insert, hand)
        four_kind.append(hand)
    
    elif hand_score == 'three_kind':
        # index_to_insert = bisect.bisect_left(three_kind, cards, key= pairwise_key)
        # three_kind.insert(index_to_insert, hand)
        three_kind.append(hand)
    
    elif hand_score == 'full_house':
        # index_to_insert = bisect.bisect_left(full_house, cards, key= pairwise_key)
        # full_house.insert(index_to_insert, hand)
        full_house.append(hand)
    
    elif hand_score == 'two_pair':
        # index_to_insert = bisect.bisect_left(two_pair, cards, key= pairwise_key)
        # two_pair.insert(index_to_insert, hand)
        two_pair.append(hand)
    
    elif hand_score == 'one_pair':
        # index_to_insert = bisect.bisect_left(one_pair, cards, key= pairwise_key)
        # one_pair.insert(index_to_insert, hand)
        one_pair.append(hand)
    
    elif hand_score == 'high_card':
        # index_to_insert = bisect.bisect_left(high_card, cards, key= pairwise_key)
        # high_card.insert(index_to_insert, hand)
        high_card.append(hand)

    else:
        print("SOMETHING HAS GONE HORRIBLY WRONG")
    
high_card_sorted = sorted(high_card, key= lambda hand: hand.cards)
one_pair_sorted = sorted(one_pair, key= lambda hand: hand.cards)
two_pair_sorted = sorted(two_pair, key= lambda hand: hand.cards)
three_kind_sorted = sorted(three_kind, key= lambda hand: hand.cards)
full_house_sorted = sorted(full_house, key= lambda hand: hand.cards)
four_kind_sorted = sorted(four_kind, key= lambda hand: hand.cards)
five_kind_sorted = sorted(five_kind, key= lambda hand: hand.cards)
    
master_list = []
# master_list.extend(high_card)
# master_list.extend(one_pair)
# master_list.extend(two_pair)
# master_list.extend(three_kind)
# master_list.extend(full_house)
# master_list.extend(four_kind)
# master_list.extend(five_kind)
master_list.extend(high_card_sorted)
master_list.extend(one_pair_sorted)
master_list.extend(two_pair_sorted)
master_list.extend(three_kind_sorted)
master_list.extend(full_house_sorted)
master_list.extend(four_kind_sorted)
master_list.extend(five_kind_sorted)

total_winnings = 0

for i in range(len(master_list)):
    total_winnings += master_list[i].bid * (i + 1)

print(total_winnings)

# print(f'Five of a kind: {five_kind}')
# print(f'Four of a kind: {four_kind}')
# print(f'Full house: {full_house}')
# print(f'Three of a kind: {three_kind}')
# print(f'Two pair: {two_pair}')
# print(f'One pair: {one_pair}')
# print(f'High card: {high_card}')