def can_escape(height, jump_height):
    current_height = 0
    fatigue = 1

    for jump in range(1, height + 1):
        #print(current_height)
        current_height += jump_height

        if current_height >= height:
            return jump
        if jump>1:
            fatigue += 0.2
        current_height -= fatigue

        if current_height < 0:
            return "Malakh failed"

    return "Malakh failed"

# Sample inputs
height, jump_height = map(int, input().split())

# Check if the beetle can escape
result = can_escape(height, jump_height)

# Output the result
if isinstance(result, int):
    print("Azadi ba", result, "paresh")
else:
    print(result)
