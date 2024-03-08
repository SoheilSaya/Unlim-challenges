# Read input values
g, y, r = map(int, input().split())
n = int(input())

# Calculate the total time for each cycle (green + yellow + red)
total_cycle_time = g + y + r

# Calculate the remaining time after dividing by total cycle time
remaining_time = n % total_cycle_time
#print(remaining_time)
# Determine the color of the traffic light after n seconds
if remaining_time==0:
    print('red')
elif remaining_time <= g:
    print("green")
elif remaining_time <= g + y:
    print("yellow")
elif remaining_time <= g + y + r:
    print("red")
