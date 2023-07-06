def solution(my_string, is_suffix):
    suffix = sorted([my_string[i:] for i in range(len(my_string))])
    return 1 if is_suffix in suffix else 0