def solution(myString):
    array = sorted(list(map(str, myString.split("x"))))
    return list(filter(lambda x: len(x), array))