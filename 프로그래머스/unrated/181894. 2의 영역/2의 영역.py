def solution(arr):
    if 2 not in arr:
        return [-1]
    else:
        a = arr.index(2)
        b = len(arr) - arr[::-1].index(2)
        return arr[a:b]