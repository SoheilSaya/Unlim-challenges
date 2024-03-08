from math import factorial
from collections import Counter
def factorial_with_zero(n):
    """
    Calculate the factorial of a number with 0 factorial being 0.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n == 0:
        return 0
    else:
        return factorial(n)

def count_bird_pairs(n, bird_types):
    """
    Count the number of different pairs of birds with the same type.

    Args:
        n (int): The number of birds.
        bird_types (list): List of bird types.

    Returns:
        int: The number of different pairs of birds.
    """
    # Count the occurrences of each bird type
    bird_counts = Counter(bird_types)
    #print(bird_counts)
    total_factorial_sum=[]
    # Calculate the sum of factorials of each count - 1 for each bird type
    for count in bird_counts.values():
        #print(count)
        if count <= 1:
            total_factorial_sum.append(0)
        else:
            total_factorial_sum.append(factorial(count) // (2 * factorial(count - 2)))
    #return pairs
    
    return sum(total_factorial_sum)

# Input
n = int(input())
bird_types = list(map(int, input().split()))

# Count the number of different pairs of birds
num_pairs = count_bird_pairs(n, bird_types)

# Output
print(num_pairs)