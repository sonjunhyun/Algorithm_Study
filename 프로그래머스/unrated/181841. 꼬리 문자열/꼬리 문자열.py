def solution(str_list, ex):
    return ''.join(list(filter(lambda x: ex not in x, str_list)))