def convert_number(number, mappings):
    for mapping in mappings:
        destination_range_start, source_range_start, range_length = mapping
        if source_range_start <= number < source_range_start + range_length:
            offset = number - source_range_start
            return destination_range_start + offset
    return number

def find_lowest_location(seeds, all_mappings):
    converted_numbers = seeds

    # Convert seeds to soil
    soil_mappings = all_mappings[0]
    converted_numbers = [convert_number(num, soil_mappings) for num in converted_numbers]

    # Convert soil to fertilizer
    fertilizer_mappings = all_mappings[1]
    converted_numbers = [convert_number(num, fertilizer_mappings) for num in converted_numbers]

    # Convert fertilizer to water
    water_mappings = all_mappings[2]
    converted_numbers = [convert_number(num, water_mappings) for num in converted_numbers]

    # Convert water to light
    light_mappings = all_mappings[3]
    converted_numbers = [convert_number(num, light_mappings) for num in converted_numbers]

    # Convert light to temperature
    temperature_mappings = all_mappings[4]
    converted_numbers = [convert_number(num, temperature_mappings) for num in converted_numbers]

    # Convert temperature to humidity
    humidity_mappings = all_mappings[5]
    converted_numbers = [convert_number(num, humidity_mappings) for num in converted_numbers]

    # Convert humidity to location
    location_mappings = all_mappings[6]
    converted_numbers = [convert_number(num, location_mappings) for num in converted_numbers]

    return min(converted_numbers)

# Read mappings from a file
mappings_file = "input.txt"  # Replace this with the actual file path
with open(mappings_file, "r") as file:
    mappings_data = file.read().splitlines()

all_mappings = []
current_mapping = []

parse_mapping = False

for line in mappings_data:
    if line.startswith("seeds:"):
        parse_mapping = False
        seeds = list(map(int, line.split()[1:]))
    elif line.startswith(("seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location")):
        parse_mapping = True
        if current_mapping:
            all_mappings.append(current_mapping)
            current_mapping = []
    elif parse_mapping and line.strip():
        mapping = tuple(map(int, line.split()))
        if len(mapping) == 3:
            current_mapping.append(mapping)

if current_mapping:
    all_mappings.append(current_mapping)

# Find the lowest location number
lowest_location = find_lowest_location(seeds, all_mappings)
print(f"The lowest location number is: {lowest_location}")