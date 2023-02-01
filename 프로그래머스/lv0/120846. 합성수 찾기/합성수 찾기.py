def solution(n):
    answer = []
    cnt = 0
    for i in range(2, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                answer.append(i)
        if answer.count(i) >= 3:
            cnt += 1
    return cnt