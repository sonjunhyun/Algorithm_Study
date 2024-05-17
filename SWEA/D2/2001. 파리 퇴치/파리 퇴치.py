T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    cnt += board[x][y]
            if cnt > max_flies:
                max_flies = cnt

    print(f"#{tc} {max_flies}")