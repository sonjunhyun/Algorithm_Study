def solution(array):
    num_count = 0
    mode = 0
    for i in set(array):
        if array.count(i) > num_count:
            num_count = array.count(i)
            mode = i
        elif array.count(i) == num_count:
            mode = -1
    return mode