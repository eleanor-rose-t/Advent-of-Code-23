def parse_input(file_content):
    card_data = []
    for line in file_content:
        parts = line.strip().split(': ')
        card_number = int(parts[0].split()[1])
        winning_numbers = set(map(int, parts[1].split(' | ')[0].split()))
        card_numbers = set(map(int, parts[1].split(' | ')[1].split()))
        card_data.append((card_number, winning_numbers, card_numbers))
    return card_data

def calculate_total_cards(data):
    card_copies = [1] * len(data)

    for index, (card_number, winning_numbers, player_numbers) in enumerate(data):
        card_multiplier = card_copies[index]
        matching_count = len(winning_numbers & player_numbers)
        for relative_position in range(1, min(matching_count + 1, len(card_copies) - index)):
            card_copies[index + relative_position] += card_multiplier

    total_cards = sum(card_copies)
    print(total_cards)

def main():
    filename = "input.txt"
    with open(filename) as file:
        lines = file.readlines()

        card_data = parse_input(lines)

        calculate_total_cards(card_data)

if __name__ == "__main__":
    main()
