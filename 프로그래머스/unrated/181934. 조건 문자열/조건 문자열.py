def solution(ineq, eq, n, m):
    new_eq = ineq + eq
    if new_eq == ">=":
        return 1 if n >= m else 0
    elif new_eq == ">!":
        return 1 if n > m else 0
    elif new_eq == "<=":
        return 1 if n <= m else 0
    else:
        return 1 if n < m else 0