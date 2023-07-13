def solution(arr):
    answer = []
    for a in arr:
        answer.extend([a]*a)
    return answer