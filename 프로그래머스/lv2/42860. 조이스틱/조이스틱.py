def solution(name):
    answer = 0
    # 기본 최소 좌우 이동 거리 (default)
    min_move = len(name) - 1
    for i, n in enumerate(name):
         # 최소 상하 이동 거리
        answer += min(ord(n) - ord("A"), ord("Z") - ord(n) + 1)
        
        # 연속된 A 문자열 탐색
        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        
        # default 좌우 이동 거리, 연속된 A 왼쪽 시작 좌우 이동 거리, 연속된 A 오른쪽 시작 좌우 이동 거리 중 최솟값 갱신
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))
    answer += min_move
    return answer