T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split()) 
    if L > X:
        answer = L - X
    else:
        if U >= X:
            answer = 0
        else:
            answer = -1
    print(f"#{tc} {answer}")