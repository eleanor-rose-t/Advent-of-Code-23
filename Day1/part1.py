def find_line_value(line):
    """
    Sums the first digit and last digit in the line.
    """
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)
    
    if first_digit is not None and last_digit is not None:
        line_value = int(first_digit + last_digit)
        return line_value
    else:
        return 0