import math

# Read input
n = int(input())
prices = list(map(int, input().split()))

# Sort prices in ascending order
prices.sort()

# Calculate number of items eligible for each discount
num_items = len(prices)
num_discount_40 = min(3, num_items)
num_discount_30 = min(5, num_items - num_discount_40)
num_discount_10 = min(1, num_items - num_discount_40 - num_discount_30)

# Apply discounts
for i in range(num_discount_40):
    prices[i] = math.ceil(prices[i] * 0.6)
for i in range(num_discount_40, num_discount_40 + num_discount_30):
    prices[i] = math.ceil(prices[i] * 0.7)
for i in range(num_discount_40 + num_discount_30, num_discount_40 + num_discount_30 + num_discount_10):
    prices[i] = math.ceil(prices[i] * 0.9)
for i in range(num_discount_40 + num_discount_30 + num_discount_10, num_items):
    prices[i] = math.ceil(prices[i] * 0.8)

# Sort discounted prices in ascending order
prices.sort()

# Output discounted prices
print(*prices)
