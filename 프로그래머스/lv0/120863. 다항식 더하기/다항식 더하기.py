def solution(polynomial):
    poly = polynomial.split(' + ')
    coef = [0, 0]
    for p in poly:
        if p.isnumeric():
            coef[1] += int(p)
        else:
            if len(p) == 1:
                coef[0] += 1
            else:
                coef[0] += int(p[:-1])
    result = []
    if coef[0]:
        if coef[0] == 1:
            result.append('x')
        else:
            result.append(f'{coef[0]}x')
    if coef[1]:
        result.append(f'{coef[1]}')
    return ' + '.join(result)