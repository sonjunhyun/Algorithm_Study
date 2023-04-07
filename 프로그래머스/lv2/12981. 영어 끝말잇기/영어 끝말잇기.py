def solution(n, words):
    answer = [0, 0]
    stack = [words[0]]
    
    for i in range(1, len(words)):
        if words[i] not in stack:
            if words[i][0] == stack[-1][-1]:
                stack.append(words[i])
            else:
                answer = [i%n+1, i//n+1]
                break
        else:
            answer = [i%n+1, i//n+1]
            break
            
    return answer