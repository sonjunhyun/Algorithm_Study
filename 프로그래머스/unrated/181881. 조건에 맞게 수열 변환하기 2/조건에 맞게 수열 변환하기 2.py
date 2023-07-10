def solution(arr):
    answer = 0
    while True:
        base = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                i /= 2
            elif i < 50 and i % 2 == 1:
                i = i * 2 + 1
            base.append(i)
        
        if base == arr:
            break
        else:
            arr = base
            answer += 1
    return answer