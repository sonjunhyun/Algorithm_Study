def solution(n):
    if n % 2:
        return sum([i for i in range(1, n+1, 2)])
    else:
        return sum([i**2 for i in range(2, n+1, 2)])