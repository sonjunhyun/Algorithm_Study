def solution(code):
    answer = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            if mode == 0:
                mode = 1
            else:
                mode = 0
        else:
            if mode == 0:
                if i % 2 == 0:
                    answer += code[i]
            if mode == 1:
                if i % 2:
                    answer += code[i]
    return answer if answer != "" else "EMPTY"