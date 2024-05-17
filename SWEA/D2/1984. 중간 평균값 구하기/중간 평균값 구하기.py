for i in range(1, int(input())+1):
    numbers = sorted([int(n) for n in input().split()])[1:-1]
    print(f"#{i} {round(sum(numbers) / len(numbers))}")