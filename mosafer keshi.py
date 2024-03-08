def count_good_rides(n, rides):
    """
    Count the number of good taxi rides in which there are exactly 2 passengers in the back seats.
    
    Args:
        n (int): Number of taxi rides.
        rides (list): List of taxi rides, each represented by a list of 3 integers (0 or 1).
    
    Returns:
        int: Number of good taxi rides.
    """
    good_rides = 0
    for ride in rides:
        if ride.count(1) == 2:  # Check if exactly 2 passengers are seated in the back seats
            good_rides += 1
    return good_rides

# Input
n = int(input())
rides = [list(map(int, input().split())) for _ in range(n)]

# Count good rides
good_rides_count = count_good_rides(n, rides)

# Output
print(good_rides_count)
