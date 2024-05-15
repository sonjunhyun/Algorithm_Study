N = int(input())
print(sorted([int(num) for num in input().split()])[(N-1)//2])