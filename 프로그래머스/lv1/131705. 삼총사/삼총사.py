import itertools

def solution(number):
    num_comb = itertools.combinations(number, 3)
    return sum([1 if sum(nums) == 0 else 0 for nums in num_comb])