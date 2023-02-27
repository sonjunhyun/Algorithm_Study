def solution(sizes):
    return max([max(w) for w in sizes]) * max([min(h) for h in sizes])