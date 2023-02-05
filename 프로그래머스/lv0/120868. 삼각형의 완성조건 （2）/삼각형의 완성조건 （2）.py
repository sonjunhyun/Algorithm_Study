def solution(sides):
    sides = sorted(sides)
    a, b = sides[0], sides[1]
    answer = [side for side in range(b-a+1, a+b)]
    return len(answer)