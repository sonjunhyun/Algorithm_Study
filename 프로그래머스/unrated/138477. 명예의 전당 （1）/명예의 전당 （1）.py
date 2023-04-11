def solution(k, score):
    answer = []
    lowest = []
    for i in range(len(score)):
        lowest.append(score[i])
        lowest.sort(reverse=True)
        if len(lowest) < k:
            answer.append(lowest[-1])
        else:
            answer.append(lowest[k-1])
    return answer