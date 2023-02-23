def solution(n):
    arr = []
    while n != 0:
        arr.append(n % 3)
        n //= 3
    answer = 0
    for i in range(1, len(arr) + 1):
        answer += pow(3, i - 1) * arr[-i]
    return answer