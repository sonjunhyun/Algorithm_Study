def solution(array):
    from collections import Counter
    counter = Counter(array).most_common()
    if len(counter) > 1:
        return -1 if counter[0][1] == counter[1][1] else counter[0][0]
    return counter[0][0]