import math

def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def get_symbol_coordinates(lines):
    symbol_coordinates = {}
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_coordinates[(x, y)] = char
                
    return symbol_coordinates
    
def get_symbol_neighbors_coordinates(symbol_coordinates, lines):
    symbol_with_neighbors_coordinates = {}
    SURROUNDS = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
    ]
    
    for x, y in symbol_coordinates:
        neighbors = []
        for x_change, y_change in SURROUNDS:
            new_x, new_y = x + x_change, y + y_change
            if 0 <= new_x < len(lines[0]) and 0 <= new_y < len(lines):
                neighbor_char = lines[new_y][new_x]
                if neighbor_char.isdigit():
                    neighbors.append((new_x, new_y))
        symbol_with_neighbors_coordinates[(x, y)] = neighbors
    
    return symbol_with_neighbors_coordinates

def calculate_part_numbers(symbol_with_neighbors_coordinates, lines):
    part_numbers = []
    visited = set()
    max_len = len(lines[0])
    symbol_neighbor_gears = {}

    for (symbol_x, symbol_y), neighbor_coordinates in symbol_with_neighbors_coordinates.items():
        for x, y in neighbor_coordinates:
            if (x, y) in visited:
                continue

            start_index = end_index = x

            while start_index >= 0 and lines[y][start_index].isdigit():
                visited.add((start_index, y))
                start_index -= 1

            while end_index < max_len and lines[y][end_index].isdigit():
                visited.add((end_index, y))
                end_index += 1

            num = int(lines[y][start_index + 1: end_index])
            part_numbers.append(num)
            
            symbol_neighbor = (symbol_x, symbol_y)
            if symbol_neighbor not in symbol_neighbor_gears:
                symbol_neighbor_gears[symbol_neighbor] = []
            symbol_neighbor_gears[symbol_neighbor].append(num)

    return sum(part_numbers)


def main():
    lines = read_input("input.txt")
    symbol_coordinates = get_symbol_coordinates(lines)
    symbol_with_neighbors_coordinates = get_symbol_neighbors_coordinates(symbol_coordinates, lines)
    answer = calculate_part_numbers(symbol_with_neighbors_coordinates, lines)
    print(answer)

if __name__ == "__main__":
    main()