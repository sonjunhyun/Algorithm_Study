def solution(a, b):
    gcd = 1
    for i in range(1, max(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    b //= gcd
    
    for i in range(2, b + 1):
        if b % i == 0:
            if i % 2 != 0 and i % 5 != 0:
                return 2
    return 1