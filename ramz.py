def align_words(letter, n, words):
    """
    Align the words vertically based on a given letter.
    
    Args:
        letter (str): The letter to align the words based on.
        n (int): Number of words.
        words (list): List of words.
    
    Returns:
        list: List of aligned words.
    """
    max_alignment_index = -1
    aligned_words = []
    
    # Find the maximum alignment index
    for word in words:
        if letter in word:
            alignment_index = word.index(letter)
            max_alignment_index = max(max_alignment_index, alignment_index)
    
    # Align the words
    for word in words:
        if letter in word:
            alignment_index = word.index(letter)
            aligned_word = '*' * (max_alignment_index - alignment_index) + word
            aligned_words.append(aligned_word)
    
    return aligned_words

# Input
letter = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Align the words
aligned_password = align_words(letter, n, words)

# Output
for word in aligned_password:
    print(word)
