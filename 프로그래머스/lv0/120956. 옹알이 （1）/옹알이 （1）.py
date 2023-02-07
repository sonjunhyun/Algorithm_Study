def solution(babbling):
    word = ['aya', 'ye', 'woo', 'ma']
    answer = []
    for i in babbling:
        for j in word:
            i = i.replace(j, ' ').strip()
        answer.append(i)
    
    cnt = 0
    for i in answer:
        if i == '':
            cnt += 1
    return cnt