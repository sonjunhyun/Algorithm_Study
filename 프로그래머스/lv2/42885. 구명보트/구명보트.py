def solution(people, limit):
    # 무게 순으로 정렬
    people.sort()
    boat = 0
    
    i = 0   # 제일 가벼운 사람의 인덱스
    j = len(people) - 1     # 제일 무거운 사람의 인덱스
    
    while i <= j:
        boat += 1
        # 가장 가벼운 사람과 무거운 사람 같이 탈출 가능한 경우
        if people[i] + people[j] <= limit:
            i += 1
        # 무거운 사람만 탈출
        j -= 1
    return boat