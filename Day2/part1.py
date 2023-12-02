def possible_games(games):
    bag = {"red": 12, "blue": 13, "green": 14}
    valid_game_ids = []
    
    for index, game in enumerate(games, start=1):
        counts = {"red": 0, "green": 0, "blue": 0}
        pulls_sets = game.split("; ")
        
        for pulls in pulls_sets:
            items = pulls.split(", ")
            for item in items:
                count, color = item.split(" ")
                counts[color] += int(count)
                
            if any(counts[color] > bag[color] for color in counts):
                break
        else:
            valid_game_ids.append(index)
                    
    return sum(valid_game_ids)

def main():
    games = []
    with open("test_input.txt") as file:
        lines = file.readlines()
        for line in lines:
            game_data = line.strip().split(": ")[1]
            games.append(game_data)
        answer = possible_games(games)
        print("Answer is: ", str(answer))
        
if __name__ == "__main__":
    main()