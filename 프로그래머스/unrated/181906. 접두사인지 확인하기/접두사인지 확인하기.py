def solution(my_string, is_prefix):
    prefix = [my_string[:i] for i in range(len(my_string))]
    return 1 if is_prefix in prefix else 0