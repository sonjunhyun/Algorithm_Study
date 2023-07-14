def solution(strArr):
    strArrlen = [len(i) for i in strArr]
    strArrlen_set = set(strArrlen)
    str_count_list = [strArrlen.count(i) for i in strArrlen_set]
    return max(str_count_list)