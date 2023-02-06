def solution(spell, dic):
    spell = ''.join(sorted(spell))
    dic_sorted = []
    for word in dic:
        dic_sorted.append(''.join(sorted(word)))
    return 1 if spell in dic_sorted else 2