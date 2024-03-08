def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def subtract_binary(bin1, bin2):
    dec1 = binary_to_decimal(bin1)
    dec2 = binary_to_decimal(bin2)
    difference = dec1 - dec2
    return decimal_to_binary(difference)

binary1, binary2 = input().split()

result = subtract_binary(binary2,binary1 )
print(binary_to_decimal(result))
