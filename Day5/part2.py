def parse_mappings(mappings_data):
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

    return seeds, all_mappings


def find_lowest_location(seeds, all_mappings):
    new_seeds = []

    for start, length in zip(seeds[::2], seeds[1::2]):
        new_seeds.append([start, start + length])

    for mapping_list in all_mappings:
        temp_seeds = []

        while len(new_seeds) > 0:
            start, end = new_seeds.pop()

            for dest, source, length in mapping_list:
                overlap_start = max(start, source)
                overlap_end = min(end, source + length)

                if overlap_start < overlap_end:
                    temp_seeds.append([
                        overlap_start - source + dest,
                        overlap_end - source + dest
                    ])
                    if overlap_start > start:
                        new_seeds.append([start, overlap_start])
                    if overlap_end < end:
                        new_seeds.append([overlap_end, end])
                    break
            else:
                temp_seeds.append([start, end])

        new_seeds = temp_seeds

    return min(new_seeds)[0]


# Read mappings from a file
mappings_file = "input.txt"
with open(mappings_file) as file:
    mappings_data = file.read().splitlines()

seeds, all_mappings = parse_mappings(mappings_data)

# Find the lowest location number
lowest_location = find_lowest_location(seeds, all_mappings)
print(f"The lowest location number is: {lowest_location}")