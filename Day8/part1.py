def read_input(file_name):
    input_lines = [x for x in open(file_name).read().strip().split('\n\n')]
    return input_lines

def parse_connections(input_lines):
    instructions = list(input_lines[0])
    connections = {}
    for line in input_lines[1].split("\n"):
        start_point = line.split(" ")[0]
        first_endpoint = line.split("(")[1].split(",")[0]
        second_endpoint = line.split(" ")[3].split(")")[0]
        connections[start_point] = (first_endpoint, second_endpoint)
    return instructions, connections

def calculate_steps(instructions, connections):
    current_position = 'AAA'
    index = 0
    while current_position != 'ZZZ':
        direction = instructions[index % len(instructions)]
        current_position = connections[current_position][0 if direction == 'L' else 1]
        index += 1
    return index

def solve_steps(start, instructions, connections):
    current_pos = start
    index = 0
    while not current_pos.endswith('Z'):
        direction = instructions[index % len(instructions)]
        current_pos = connections[current_pos][0 if direction == 'L' else 1]
        index += 1
    return index

def main(): 
    file_name = "test_input_1.txt"
    input_lines = read_input(file_name)
    inst, conn = parse_connections(input_lines)

    result = calculate_steps(inst, conn)
    print("Part 1: " + str(result))
    
if __name__ == "__main__":
    main()


