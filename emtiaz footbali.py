def calculate_score(wins, draws, losses):
    """
    Calculate the total score of a team based on the number of wins, draws, and losses.
    
    Args:
        wins (int): Number of wins.
        draws (int): Number of draws.
        losses (int): Number of losses.
    
    Returns:
        int: Total score of the team.
    """
    return (wins * 3) + (draws * 1)

# Input
w, d, l = map(int, input().split())

# Calculate score
total_score = calculate_score(w, d, l)

# Output
print(total_score)
