T = int(input())
for tc in range(1, T+1):
    hay = []
    N = int(input())
    for _ in range(N):
        x = int(input())
        hay.append(x)
        
    avg_hay = sum(hay) // N
    answer = 0
    for h in sorted(hay):
        if h < avg_hay:
            answer += avg_hay - h
            
    print(f"#{tc} {answer}")
        