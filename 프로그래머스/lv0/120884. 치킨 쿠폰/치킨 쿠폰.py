def solution(chicken):
    answer = 0
    while chicken >= 10:
        a = chicken // 10
        b = chicken % 10
        answer += a
        chicken = a + b
    return answer