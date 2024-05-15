T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    hour = A + B if A + B < 24 else A + B - 24
    print(f"#{tc} {hour}")