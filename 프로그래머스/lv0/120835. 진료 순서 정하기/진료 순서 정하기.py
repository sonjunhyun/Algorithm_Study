def solution(emergency):
    answer = []
    emg_rnk = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(emg_rnk.index(i)+1)
    return answer