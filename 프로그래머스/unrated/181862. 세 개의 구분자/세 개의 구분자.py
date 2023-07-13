def solution(myStr):
    result = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').strip().split()
    return result if result else ["EMPTY"]