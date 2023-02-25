def solution(s):
    cnt, zero = 0, 0
    while s != 1:
        if s == '1':
            break
        cnt += 1
        zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
    return [cnt, zero]