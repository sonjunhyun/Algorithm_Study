def solution(dots):
    dots = sorted(dots)
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    slope1 = (y[1]-y[0])/(x[1]-x[0])
    slope2 = (y[3]-y[2])/(x[3]-x[2])
    return 1 if slope1 == slope2 else 0