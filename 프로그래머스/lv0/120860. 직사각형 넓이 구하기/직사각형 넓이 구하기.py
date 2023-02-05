def solution(dots):
    x_dot = [dot[0] for dot in dots]
    y_dot = [dot[1] for dot in dots]
    base = max(x_dot) - min(x_dot)
    height = max(y_dot) - min(y_dot)
    return base * height