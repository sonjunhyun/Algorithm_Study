def solution(arr, query):
    for q in range(len(query)):
        if q % 2:
            arr = arr[query[q]:]
        else:
            arr = arr[:query[q]+1]
    return arr