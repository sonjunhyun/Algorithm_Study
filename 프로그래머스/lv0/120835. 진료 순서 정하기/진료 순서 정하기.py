def solution(emergency):
    emg_rnk = sorted(emergency, reverse=True)
    return [emg_rnk.index(i)+1 for i in emergency]