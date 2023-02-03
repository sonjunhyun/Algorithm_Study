def solution(array, n):
    subs = []
    array.sort()
    for num in array:
        subs.append(abs(n - num))
    nearest = [array[subs.index(min(subs))]]
    
    return nearest if len(nearest) != 1 else nearest[0]