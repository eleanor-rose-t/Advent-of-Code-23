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
    
def find_sum(filename):
    """
    Sums the line values of each line in the file.
    """
    with open(filename) as file:
        lines = file.readlines()
        line_values = [find_line_value(line.strip()) for line in lines]
        total_sum = sum(line_values)
        return total_sum
    
def main():
    total_sum = find_sum("test_input.txt")
    print(total_sum)
    
if __name__ == "__main__":
    main()