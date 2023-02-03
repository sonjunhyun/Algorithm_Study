def solution(s):
    answer = []
    for i in str(s):
        if str(s).count(i) == 1:
            answer.append(i)
    return ''.join(sorted(answer))