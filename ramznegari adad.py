def numbers_within_numbers(n):
    n_str = str(n)
    result = ''
    count = 1

    for i in range(1, len(n_str)):
        if n_str[i] == n_str[i-1]:
            count += 1
        else:
            result += str(count) + n_str[i-1]
            count = 1

    result += str(count) + n_str[-1]

    if int(result) % 2 == 0:
        return int(result) // 2
    else:
        return int(result) * 3

def main():
    n = int(input().strip())
    if n == 0:
        print(30)
    else:
        encoded_number = numbers_within_numbers(n)
        print(encoded_number)

if __name__ == "__main__":
    main()
