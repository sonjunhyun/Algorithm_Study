def solution(arr, k):
    random_set = set()
    result = []
    
    for num in arr:
        random_set.add(num)
        if len(random_set) == k:
            break
    
    for num in arr:
        if num in random_set:
            result.append(num)
            random_set.remove(num)
    
    while len(result) < k:
        result.append(-1)
    
    return result