def min_additional_floors(n, building_floors):
    floor_counts = {}
    additional_floors = 0
    
    for floor in building_floors:
        if floor in floor_counts:
            # Increment floor count until it's unique
            while floor in floor_counts:
                floor += 1
                additional_floors += 1
        
        # Update floor count dictionary
        floor_counts[floor] = 1
    
    return additional_floors

# Input
n = int(input())
building_floors = list(map(int, input().split()))

# Calculate the minimum additional floors needed
result = min_additional_floors(n, building_floors)

# Output the result
print(result)
