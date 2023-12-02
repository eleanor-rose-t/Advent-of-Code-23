import re

def find_line_value(line):
    """
    Sums the first digit and last digit in the line accounting for spelled out digits.
    """
    spelled_out_digits = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    pattern = r'(?:\d|one|two|three|four|five|six|seven|eight|nine)'

    matches = re.findall(pattern, line, re.IGNORECASE)
    print(matches)

    if matches:
        first_digit = matches[0]
        if not first_digit.isdigit():
            first_digit = spelled_out_digits.get(first_digit)
        last_digit = matches[-1]
        if not last_digit.isdigit():
            last_digit = spelled_out_digits.get(last_digit)
    
    return int(first_digit + last_digit)


def find_sum(filename):
    """
    Sums the line values of each line in the file.
    """
    sum = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            line_value = find_line_value(line)
            sum += line_value
        return sum
    
def main():
    total_sum = find_sum("test_input.txt")
    print(total_sum)
    
if __name__ == "__main__":
    main()