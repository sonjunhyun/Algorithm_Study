# 문자열 Slicing
def solution(A, B):
    for push in range(len(A)):
        if A == B:
            return push
        else:
            A = A[-1] + A[:-1]
            push += 1
    return -1

# insert, pop 활용
def solution(A, B):
    A, B = list(A), list(B)
    for push in range(len(A)):
        if A == B:
            return push
        else:
            A.insert(0, A.pop())
    return -1

# find 활용
def solution(A, B):
    return B*2.find(A)
