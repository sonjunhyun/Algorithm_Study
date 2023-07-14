def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if answer and arr[i] == answer[-1]:
            answer.pop()
        else:
            answer.append(arr[i])
    return answer if len(answer) else [-1]