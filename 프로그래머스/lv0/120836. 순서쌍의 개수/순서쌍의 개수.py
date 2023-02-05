def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))