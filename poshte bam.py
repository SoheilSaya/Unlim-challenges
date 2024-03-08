def find_next_tallest(n, heights):
    result = []
    for i in range(n):
        found = False
        for j in range(i + 1, n):
            if heights[j] > heights[i]:
                result.append(heights[j])
                found = True
                break
        if not found:
            result.append(-1)
    return result

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    
    result = find_next_tallest(n, heights)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
