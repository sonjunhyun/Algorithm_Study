def solution(myString, pat):
    return myString.rsplit(pat, 1)[0] + pat
    # rsplit(separator, maxsplit): separator 기준으로 maxsplit만큼 쪼갠다.