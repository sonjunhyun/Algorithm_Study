def solution(arr):
    answer = arr
    power_of_two = [2**i for i in range(11)]
    while len(answer) not in power_of_two:
        answer.append(0)
    return answer