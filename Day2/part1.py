def parse_input(input_lines):
    games = {}
    for line in input_lines:
        game_id, draws = line.split(": ")
        game_id = int(game_id.split()[1])
        games[game_id] = []
        
        individual_draws = draws.split("; ")
        for draw in individual_draws:
            draw_data = {}
            for draw_info in draw.split(", "):
                count, color = draw_info.split()
                draw_data[color] = int(count)
            games[game_id].append(draw_data)
    
    return games

def possible_games(games):
    available = {"red": 12, "green": 13, "blue": 14}
    total = 0
    for game_id, game_draws in games.items():
        if all(all(draw[color] <= available[color] for color in draw) for draw in game_draws):
            total += game_id
    return total
    
def main():
    with open("input.txt") as file:
        input_lines = file.readlines()
    
    data = parse_input(input_lines)
    result = possible_games(data)
    print(result)
    
if __name__ == "__main__":
    main()
