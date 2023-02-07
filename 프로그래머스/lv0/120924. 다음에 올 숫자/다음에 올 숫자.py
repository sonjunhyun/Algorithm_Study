def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]
        return common[-1] + d
    else:
        p = common[1] // common[0]
        return common[-1] * p
        