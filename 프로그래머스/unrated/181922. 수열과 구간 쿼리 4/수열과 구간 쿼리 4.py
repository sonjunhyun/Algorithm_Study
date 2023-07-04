def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        arr_new = list(range(s, e+1))
        for i in arr_new:
            if i % k == 0:
                arr[i] += 1
    return arr