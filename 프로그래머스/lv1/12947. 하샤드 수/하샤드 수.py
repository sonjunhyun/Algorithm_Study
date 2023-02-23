def solution(x):
    div = 0
    for i in str(x):
        div += int(i)
    return False if x % div else True