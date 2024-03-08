def correct_digit(digit):
    """
    Correct the given digit according to the keyboard malfunction described.
    """
    mapping = {'2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '1': '9'}
    return mapping.get(digit, digit)

def correct_number(number):
    """
    Correct the digits of the given number according to the keyboard malfunction described.
    """
    corrected_number = ''.join(correct_digit(digit) for digit in str(number))
    return int(corrected_number)

# Input
n, m = input().split('+')
n = int(n.strip())
m = int(m.strip())

# Correct the numbers
corrected_n = correct_number(n)
corrected_m = correct_number(m)

# Output
print(corrected_n + corrected_m)
