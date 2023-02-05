def solution(my_string):
    answer = 0
    number_string = ""
    for c in my_string:
        if c.isdecimal():
            number_string += c
        else:
            if number_string == "":
                pass
            else:
                answer += int(number_string)
                number_string = ""
    if not number_string == "":
        answer += int(number_string)
    return answer
    