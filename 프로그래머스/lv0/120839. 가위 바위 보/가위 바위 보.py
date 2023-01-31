def solution(rsp):
    win_list = {'2': '0', '0': '5', '5': '2'}
    return "".join(win_list[i] for i in rsp)