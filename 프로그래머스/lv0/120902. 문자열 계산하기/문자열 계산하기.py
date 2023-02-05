def solution(my_string):
    number_string = my_string.split()
    answer = int(number_string[0])
    for i in range(1, len(number_string), 2):
        if number_string[i] == '+':
            answer += int(number_string[i+1])
        else:
            answer -= int(number_string[i+1])
    return answer

#내장함수 eval 활용
def solution(my_string):
    return eval(my_string)
