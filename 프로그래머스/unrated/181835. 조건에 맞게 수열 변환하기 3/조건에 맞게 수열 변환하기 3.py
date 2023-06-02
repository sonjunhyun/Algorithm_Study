def solution(arr, k):
    if k % 2:
        return [i * k for i in arr]
    return [i + k for i in arr]