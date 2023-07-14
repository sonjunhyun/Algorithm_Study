def solution(rank, attendance):
    students = sorted([i for i, j in zip(rank, attendance) if int(j)])
    a, b, c = rank.index(students[0]), rank.index(students[1]), rank.index(students[2])
    return 10000 * a + 100 * b + c