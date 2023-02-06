def solution(score):
    average = [sum(i)/len(i) for i in score]
    sorted_avg = sorted(average, reverse=True)
    rank = []
    for i in average:
        rank.append(sorted_avg.index(i) + 1)
    return rank