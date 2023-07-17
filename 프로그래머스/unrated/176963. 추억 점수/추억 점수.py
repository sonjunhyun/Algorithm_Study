# 내 풀이
def solution(name, yearning, photo):
    answer = []
    score_list = dict([(i, j) for i, j in zip(name, yearning)]) # name, yearning 딕셔너리로 변환
    for p in photo:
        score = 0   # score 초기화
        for i in p:
            if score_list.get(i):   # score_list의 key값이라면,
                score += score_list.get(i)  # score에 key값에 해당하는 value 더해준다.
        answer.append(score)    # 합한 score를 answer 리스트에 추가
    return answer

# 코드 간결화
def solution(name, yearning, photo):
    answer = []
    score_dict = dict(zip(name, yearning))    # 굳이 list로 만들고 dictionary로 자료형 변환 필요 x
    for p in photo:
        score = 0
        for i in p:
            if i in score_dict:    # score_dict에 있는 값이면,
                score += score_dict[i]    # 해당하는 value 더해준다.
        answer.append(score)    # 합한 score를 answer 리스트에 추가
    return answer
