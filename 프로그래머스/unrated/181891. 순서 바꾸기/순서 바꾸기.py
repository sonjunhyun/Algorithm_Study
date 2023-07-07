def solution(num_list, n):
    a = num_list[n:]
    a.extend(num_list[:n])
    return a