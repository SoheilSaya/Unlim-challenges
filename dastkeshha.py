# Function to calculate the minimum gloves needed
def min_gloves_needed(r, b, y, g):
    min_count = min(r, b, y, g)
    return r + b + y + g - min_count + 2

# Input
r, b, y, g = map(int, input().split())

# Calculate the minimum gloves needed
result = min_gloves_needed(r, b, y, g)

# Output the result
print(result)
