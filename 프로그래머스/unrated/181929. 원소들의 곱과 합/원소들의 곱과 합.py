def solution(num_list):
    a = 1
    for num in num_list:
        a *= num
    b = sum(num_list)**2
    return 1 if a < b else 0