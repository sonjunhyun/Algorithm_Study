def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        div_arr = [x for x in range(1, i + 1) if i % x == 0]
        if len(div_arr) % 2:
            answer -= i
        else:
            answer += i
    return answer