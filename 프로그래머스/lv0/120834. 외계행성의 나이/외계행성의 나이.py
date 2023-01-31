def solution(age):
    answer = ''
    alphabet = 'abcdefghij'
    for i in str(age):
        answer += alphabet[int(i)] 
    return answer