def select_georges_food(n):
    menu = ["pizza", "burger", "fries potato", "hotdog"]
    selected_food = []
    for i in range(n):
        selected_food.append(menu[i % 4])
    return selected_food

def main():
    n = int(input())
    selected_food = select_georges_food(n)
    for food in selected_food:
        print(food)

if __name__ == "__main__":
    main()
