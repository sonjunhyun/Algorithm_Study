def solution(A, B):
    for push in range(len(A)):
        if A == B:
            return push
        else:
            A = A[-1] + A[:-1]
            push += 1
    return -1
        