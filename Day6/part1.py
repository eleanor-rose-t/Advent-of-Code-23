def read_input(file_name):
    with open(file_name) as file:
        input_list = file.read().splitlines()
    return input_list


def extract_values(input_list):
    times = [int(x) for x in input_list[0].split() if x.isdigit()]
    distances = [int(x) for x in input_list[1].split() if x.isdigit()]
    return times, distances


def calculate_number_of_ways(times, distances):
    number_of_ways = []

    for i, milliseconds in enumerate(times):
        goal_distance = distances[i]
        ways = 0
        for holding in range(milliseconds + 1):
            if holding * (milliseconds - holding) > goal_distance:
                ways += 1
        number_of_ways.append(ways)

    return number_of_ways


def main():
    file_name = "input.txt"
    
    input_list = read_input(file_name)
    times, distances = extract_values(input_list)
    number_of_ways = calculate_number_of_ways(times, distances)

    result = number_of_ways[0] * number_of_ways[1] * number_of_ways[2] * number_of_ways[3]
    print(result)


if __name__ == "__main__":
    main()

