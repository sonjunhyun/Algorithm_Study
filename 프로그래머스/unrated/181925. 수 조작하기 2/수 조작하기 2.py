def solution(numLog):
    log = [numLog[i] - numLog[i - 1] for i in range(1, len(numLog))]
    result_dict = {1: "w", -1: "s", 10: "d", -10: "a"}
    answer = ''
    for l in log:
        answer += result_dict[l]
    return answer