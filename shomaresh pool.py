def separate_digits(number):
    """
    Separate digits of the number with commas every three digits from the right side.
    
    Args:
        number (int): The number to be separated.
    
    Returns:
        str: The separated number as a string.
    """
    # Convert the number to a string
    number_str = str(number)
    
    # Initialize variables to store the separated number and the counter
    separated_number = ""
    counter = 0
    
    # Iterate over the string from right to left
    for digit in reversed(number_str):
        # Insert a comma after every third digit from the right side
        if counter == 3:
            separated_number = ',' + separated_number
            counter = 0
        separated_number = digit + separated_number
        counter += 1
    
    return separated_number

# Input
n = int(input())

# Separate digits
separated_n = separate_digits(n)

# Output
print(separated_n)
