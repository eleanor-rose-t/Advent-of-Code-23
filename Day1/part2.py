def find_line_value(line):
    """
    Sums the first digit and last digit in the line accounting for spelled out digits.
    """
    spelled_out_digits = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    first_digit = next((char for char in line if char.isdigit() or char in spelled_out_digits), None)
    last_digit = next((char for char in reversed(line) if char.isdigit() or char in spelled_out_digits), None)
    
    if first_digit is not None and last_digit is not None:
        line_value = int(first_digit + last_digit)
        return line_value
    else:
        return 0