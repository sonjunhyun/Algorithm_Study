def solution(box, n):
    num = 1
    for i in box:
        x = i // n
        num *= x
    return num