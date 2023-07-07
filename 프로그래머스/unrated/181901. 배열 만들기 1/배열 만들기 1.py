def solution(n, k):
    # return [i for i in range(1, n+1) if i % k == 0]
    return list(filter(lambda x: x % k == 0, range(1, n+1)))