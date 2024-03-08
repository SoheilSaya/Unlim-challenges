def is_cool(username):
    """
    Check if the username is cool or not.

    Args:
        username (str): The username to check.

    Returns:
        str: 'cool' if the username is cool, 'not cool' otherwise.
    """
    char_count = {}
    for char in username:
        char_count[char] = char_count.get(char, 0) + 1
    
    for count in char_count.values():
        if count < 2:
            return 'not cool'
    return 'cool'

# Input
username = input()

# Check if the username is cool
result = is_cool(username)

# Output
print(result)
