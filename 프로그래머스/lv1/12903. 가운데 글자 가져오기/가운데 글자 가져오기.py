def solution(s):
    if len(s) % 2:
        return s[len(s) // 2]
    else:
        return s[(len(s) - 1) // 2] + s[len(s) // 2]