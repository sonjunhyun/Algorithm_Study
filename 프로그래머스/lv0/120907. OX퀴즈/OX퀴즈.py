def solution(quiz):
    answer = []
    for i in quiz:
        answer.append('O' if eval(i.replace('=', '==')) else 'X')
    return answer