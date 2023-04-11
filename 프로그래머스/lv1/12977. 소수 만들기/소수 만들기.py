from itertools import combinations

def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False
        return True
    
def solution(nums):
    comb = list(combinations(nums, 3))
    count = 0
    
    for c in comb:
        if is_prime_number(sum(c)):
            count += 1
            
    return count