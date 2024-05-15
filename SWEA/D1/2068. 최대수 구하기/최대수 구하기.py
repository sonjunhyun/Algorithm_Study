for i in range(1, int(input())+1):
    maximum = max([int(num) for num in input().split()])
    print(f"#{i} {maximum}")