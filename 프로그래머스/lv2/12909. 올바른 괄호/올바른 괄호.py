def solution(s):
    num = 0
    for g in s:
        if g == '(':
            num += 1
        else:
            if num > 0:
                num -= 1
            else:
                return False
    return num == 0