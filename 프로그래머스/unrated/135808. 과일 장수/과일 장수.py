def solution(k, m, score):
    revenue = 0     # revenue 0으로 초기화
    score.sort(reverse=True)    # score 리스트 내림차순 정렬
    boxes = [score[i*m:(i+1)*m] for i in range(len(score)//m)]  # m개씩 담을 수 있는 box 리스트 생성
    for box in boxes:
        revenue += min(box) * m  # box 당 이익(box 안 최저 사과 점수 * 사과 개수(m)) 구한 뒤 revenue에 더해준다.
    return revenue