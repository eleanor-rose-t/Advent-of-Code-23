def find_line_value(line):
    """
    Sums the first digit and last digit in the line accounting for spelled out digits.
    """
    spelled_out_digits = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    first_digit = next((char for char in line.split() if char.isdigit() or char in spelled_out_digits), None)
    last_digit = next((char for char in reversed(line.split()) if char.isdigit() or char in spelled_out_digits), None)
    
    if first_digit in spelled_out_digits:
        first_digit = spelled_out_digits[first_digit]
        
    if last_digit in spelled_out_digits:
        last_digit = spelled_out_digits[last_digit]
    
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
    total_sum = find_sum("input.txt")
    print(total_sum)
    
if __name__ == "__main__":
    main()