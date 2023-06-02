def solution(num_list):
    num_list = [1 if num >= 0 else 0 for num in num_list]
    if 0 in num_list:
        return num_list.index(0)
    return -1