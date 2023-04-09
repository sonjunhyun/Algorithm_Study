def solution(strings, n):
    new = sorted([i[n] + i for i in strings])
    answer = []
    for v in new:
        answer.append(v[1:])
    return answer