def solution(n):
        # 이차원 배열 초기화
    arr = [[0] * n for _ in range(n)]
    # 상하좌우 방향을 나타내는 리스트
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 현재 위치와 값을 나타내는 변수 초기화
    x, y = 0, 0
    num = 1
    direction_idx = 0

    for _ in range(1, n * n + 1):
        arr[x][y] = num
        num += 1

        # 다음 위치 계산
        dx, dy = directions[direction_idx]
        nx, ny = x + dx, y + dy

        # 다음 위치가 배열 범위를 벗어나거나 이미 값이 채워져 있는 경우 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
            direction_idx = (direction_idx + 1) % 4
            dx, dy = directions[direction_idx]
            nx, ny = x + dx, y + dy

        x, y = nx, ny

    return arr