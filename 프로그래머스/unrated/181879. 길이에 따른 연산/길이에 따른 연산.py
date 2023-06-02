def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    else:
        return eval('*'.join([str(num) for num in num_list]))