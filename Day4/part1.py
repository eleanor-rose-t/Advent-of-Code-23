def calculate_points(cards):
    total_points = 0
    
    for card in cards:
        card = card.split(": ")[1]
        winning_numbers, card_numbers = card.split(" | ")
        winning_numbers = winning_numbers.split()
        card_numbers = card_numbers.split()
        
        points = 0
        matched_numbers = set()
        
        for number in card_numbers:
            if number in winning_numbers and number not in matched_numbers:
                matched_numbers.add(number)
                points += 1

        if points > 0:
            total_points += 2 ** (points - 1)  # Calculate points based on matches

    return total_points

def read_input(filename):
    with open(filename) as file:
        card_lines = [line.strip() for line in file]
    return card_lines

def main():
    filename = "input.txt"
    cards = read_input(filename)
    total_points = calculate_points(cards)
    print(total_points)
    
if __name__ == "__main__":
    main()