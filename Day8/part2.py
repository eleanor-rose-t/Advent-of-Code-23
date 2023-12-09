import math

def read_input(file_name):
    with open(file_name) as file:
        sections = file.read().strip().split('\n\n')
    return sections

def parse_connections(input_lines):
    instructions = list(input_lines[0])
    connections = {}
    for line in input_lines[1].split("\n"):
        start_point = line.split(" ")[0]
        first_endpoint = line.split("(")[1].split(",")[0]
        second_endpoint = line.split(" ")[3].split(")")[0]
        connections[start_point] = (first_endpoint, second_endpoint)
    return instructions, connections

def solve_steps(start, instructions, connections):
    current_pos = start
    index = 0
    while not current_pos.endswith('Z'):
        direction = instructions[index % len(instructions)]
        current_pos = connections[current_pos][0 if direction == 'L' else 1]
        index += 1
    return index

def calculate_lcm_for_A_endpoints(conn, inst):
    lcm_result = 1
    for start_pos in conn:
        if start_pos.endswith('A'):
            lcm_result = math.lcm(lcm_result, solve_steps(start_pos, inst, conn))
    return lcm_result

def main():
    file_name = "input.txt"
    sections = read_input(file_name)
    inst, conn = parse_connections(sections)

    result = calculate_lcm_for_A_endpoints(conn, inst)
    print("Part 2: " + str(result))

if __name__ == "__main__":
    main()
