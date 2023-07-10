def solution(myString, pat):
    newString = []
    for i in myString:
        if i == "A":
            newString.append("B")
        else:
            newString.append("A")
    return 1 if pat in ''.join(newString) else 0