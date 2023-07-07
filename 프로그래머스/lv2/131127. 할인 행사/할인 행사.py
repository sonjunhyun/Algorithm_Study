from collections import Counter

def solution(want, number, discount):    
    wishlist = Counter(dict(zip(want, number)))
    answer = 0
    
    for i in range(len(discount)-9):
        if wishlist == Counter(discount[i:i+10]):
            answer += 1
    return answer