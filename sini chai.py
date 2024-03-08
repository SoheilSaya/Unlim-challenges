import math

def calculate_trips(total_guests, double_tea_guests):
    """
    Calculate the number of trips Mohsen needs to make to serve tea to all guests.
    
    Args:
        total_guests (int): Total number of guests.
        double_tea_guests (int): Number of guests who want two cups of tea.
    
    Returns:
        int: Number of trips Mohsen needs to make.
    """
    # Calculate total cups of tea required
    total_cups_of_tea = total_guests + double_tea_guests
    
    # Calculate number of trips needed
    trips = math.ceil(total_cups_of_tea / 9)
    
    return trips

# Input
total_guests, double_tea_guests = map(int, input().split())

# Calculate trips
trips_needed = calculate_trips(total_guests, double_tea_guests)

# Output
print(trips_needed)
