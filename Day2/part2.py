import math

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

def find_minimum_set_power(games):
    colors = ("red", "green", "blue")
    total = 0
    for game in games.values():
        total += math.prod(max(_.get(color, 0) for _ in game) for color in colors)
    return total

def main():
    with open("input.txt") as file:
        input_lines = file.readlines()
    
    data = parse_input(input_lines)
    result = find_minimum_set_power(data)
    print(result)
    
if __name__ == "__main__":
    main()