def solution(s):
    stack = [s[0]]
    for v in s[1:]:
        if len(stack) > 0 and v == stack[-1]:
            stack.pop()
        else:
            stack.append(v)
    return 0 if len(stack) else 1