def solution(array, n):
    cnt = 0
    for i in array:
        if i == n:
            cnt += 1
    return cnt