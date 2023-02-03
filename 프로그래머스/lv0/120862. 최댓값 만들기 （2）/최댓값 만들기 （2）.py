def solution(numbers):
    numbers = sorted(numbers)
    max_candidates = [numbers[0] * numbers[1], numbers[-1] * numbers[-2]]
    return max(max_candidates)