# Function to calculate distance given speed and time
def calculate_distance(speed, time):
    return speed * time / 60

# Function to calculate speed given distance and time
def calculate_speed(distance, time):
    return distance /1000 * 60 / time

# Function to calculate time given distance and speed
def calculate_time(distance, speed):
    return (distance/1000) / (speed)

# Function to calculate fuel consumption given distance and fuel_per_100km
def calculate_fuel(distance, fuel_per_100km):
    return distance * fuel_per_100km / 100000
# Number of commands
n = int(input())

# Lists to store the results
results = []

# Process each command
for _ in range(n):
    command, param1, param2 = input().split()

    if command == 'distance':
        distance = calculate_distance(int(param1), int(param2))
        results.append('{:.1f}km'.format(distance))
    elif command == 'speed':
        speed = calculate_speed(int(param1), int(param2))
        results.append('{:.1f}km/h'.format(speed))
    elif command == 'time':
        time = calculate_time(int(param1), int(param2))
        results.append('{:.1f}h'.format(time))
    elif command == 'fuel':
        fuel = calculate_fuel(int(param1), int(param2))
        results.append('{:.1f}L'.format(fuel))

# Print all results together
for result in results:
    print(result)