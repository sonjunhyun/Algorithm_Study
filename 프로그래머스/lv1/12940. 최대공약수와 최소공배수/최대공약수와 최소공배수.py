def solution(n, m):
    a = max([i for i in range(1, n + 1) if n % i == 0 and m % i == 0])
    b = min([j for j in range(1, n * m + 1) if j % n == 0 and j % m == 0])
    return [a, b]