def solution(cards1, cards2, goal):
    for g in goal:
        if cards1 and g == cards1[0]:   # cards1이 비어있지 않고 cards1의 첫 번째 요소와 같다면,
            cards1.pop(0)   # cards1에서 첫 번째 요소 제거
        elif cards2 and g == cards2[0]: # cards2이 비어있지 않고 cards2의 첫 번째 요소와 같다면,
            cards2.pop(0)   # cards2에서 첫 번재 요소 제거
        else:   # cards1, cards2 둘 중 어느 한 곳의 첫 번째 요소와 같지 않다면 'No' 반환
            return 'No'
    return 'Yes'    # goal의 모든 요소 탐색이 끝나면 'Yes' 반환