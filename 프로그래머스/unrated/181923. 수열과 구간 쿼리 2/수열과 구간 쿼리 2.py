def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        new_arr = list(filter(lambda x: x > k, sorted(arr[s:e+1])))
        if len(new_arr) > 0:
            answer.append(new_arr[0])
        else:
            answer.append(-1)
    return answer