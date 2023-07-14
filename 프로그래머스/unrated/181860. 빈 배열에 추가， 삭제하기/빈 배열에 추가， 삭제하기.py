def solution(arr, flag):
    answer = []
    for a, b in zip(arr, flag):
        if b == True:
            answer.extend([a]*a*2)
        else:
            for i in range(a):
                answer.pop()
    return answer