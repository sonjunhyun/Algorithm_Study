def solution(a, b):
    return sum(x for x in range(a, b + 1)) if a <= b else sum(x for x in range(b, a + 1))