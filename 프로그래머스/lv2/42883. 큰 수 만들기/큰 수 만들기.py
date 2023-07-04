def solution(number, k):
    answer = []
    for i, num in enumerate(number):
        while answer and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
        answer.append(num)
    answer = answer[:len(number)-k]
    return "".join(answer)