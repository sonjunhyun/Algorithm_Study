def solution(hp):
    ant = [5, 3, 1]
    ant_num = 0
    for i in range(len(ant)):
        ant_num += hp // ant[i]
        hp %= ant[i]
    return ant_num