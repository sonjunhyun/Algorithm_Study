T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    gcd = 1
    if A == B:
        gcd = B
    print(f"#{tc} {gcd}")