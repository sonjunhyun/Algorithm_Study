def solution(t, p):
    return sum([int(t[i:i+len(p)]) <= int(p) for i in range(len(t)-len(p)+1)])