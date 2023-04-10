def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i)*(food[i]//2)
    rev_answer = ''.join(reversed(answer))
    answer += '0' + rev_answer
    return answer