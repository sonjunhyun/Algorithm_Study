def solution(n):
    cnt_1 = str(bin(n)).count('1')
    while True:
        n += 1
        cnt_2 = str(bin(n)).count('1')
        if cnt_1 == cnt_2:
            break
    return n