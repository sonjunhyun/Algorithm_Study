def solution(n):
    arr = list(str(n))
    arr = sorted(arr, reverse=True)
    return int(''.join(arr))