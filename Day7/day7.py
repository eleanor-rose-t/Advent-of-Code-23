def get_hands_from_file(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file if line.strip()]
    return [(hand, int(bid)) for line in lines for hand, bid in [line.split()]]

def count_values(hand):
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    return tuple(sorted(counts.values()))

def convert(hand, part1):
    if part1:
        hand = hand.replace('J', 'X')
    hand_values = ['J23456789TXQKA'.index(card) for card in hand]
    counts = []
    for rank in 'J23456789TQKA':
        hand_type = count_values(hand.replace('J', rank))
        possible_types = [(1, 1, 1, 1, 1), (1, 1, 1, 2), (1, 2, 2), (1, 1, 3), (2, 3), (1, 4), (5,)]
        hand_type_index = possible_types.index(hand_type)
        counts.append(hand_type_index)
    return max(counts), *hand_values

def calculate_winnings(filename):
    hands = get_hands_from_file(filename)
    
    for part1 in (True, False):
        converted_hands = sorted((convert(hand, part1), bid) for hand, bid in hands)
        total_winnings = sum(i * bid + bid for i, (_, bid) in enumerate(converted_hands))
        print('Part ' + str(2 - int(part1)) + ': ' + str(total_winnings))

if __name__ == "__main__":
    input_filename = 'input.txt'
    calculate_winnings(input_filename)
