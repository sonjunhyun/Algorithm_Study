def solution(N, stages):
    n = len(stages)
    answer = []
    
    for i in range(1, N+1):
        if n != 0:
            answer.append((i, stages.count(i)/n))
            n -= stages.count(i)
        else:
            answer.append((i, 0))
    
    answer.sort(key=lambda x: x[1], reverse=True)
    result = [x[0] for x in answer]
    return result
