def solution(str_list):
    idx_l, idx_r = 100, 100
    
    if "l" in str_list:
        idx_l = str_list.index("l")
    if "r" in str_list:
        idx_r = str_list.index("r")
        
    if idx_l < idx_r:
        return str_list[:idx_l]
    elif idx_l > idx_r:
        return str_list[idx_r+1:]
    else:
        return list()