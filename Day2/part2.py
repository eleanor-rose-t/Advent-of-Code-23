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

