def solution(i, j, k):
    nums = [str(x) for x in range(i, j + 1)]
    return ''.join(nums).count(str(k))