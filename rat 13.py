def encrypt(text):
    """
    Encrypts the text by shifting each letter by 13 positions.

    Args:
        text (str): The text to encrypt.

    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif char.isupper():
            encrypted_text += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

# Input
text = input()

# Encrypt the text
encrypted_text = encrypt(text)

# Output
print(encrypted_text)
