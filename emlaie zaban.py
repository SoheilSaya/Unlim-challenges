def can_form_word(word, letters):
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    for char in word:
        if char not in letter_count or letter_count[char] == 0:
            return False
        letter_count[char] -= 1
    
    return True

def can_form_number(number, digits):
    digit_count = {}
    for digit in digits:
        digit_count[digit] = digit_count.get(digit, 0) + 1
    
    for char in number:
        if char not in digit_count or digit_count[char] == 0:
            return False
        digit_count[char] -= 1
    
    return True

def main():
    mixed_input = input().strip()
    word, number = input().strip().split()
    
    letters = [char for char in mixed_input if char.isalpha()]
    digits = [char for char in mixed_input if char.isdigit()]
    
    can_form_word_result = can_form_word(word, letters)
    can_form_number_result = can_form_number(number, digits)
    
    print(can_form_word_result)
    print(can_form_number_result)

if __name__ == "__main__":
    main()
