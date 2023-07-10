def solution(myString):
    return list(map(lambda x: len(x), list(map(str, myString.split("x")))))