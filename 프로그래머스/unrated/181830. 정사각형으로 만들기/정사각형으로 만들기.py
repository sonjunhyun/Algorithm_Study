def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for r in range(row):
            arr[r].extend([0]*(row-col))
    elif row < col:
        arr.extend([[0]*col]*(col-row))
    return arr