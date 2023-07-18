def solution(nums):
    pokemon_cnt = 0     # 가져갈 수 있는 pokemon 수 0으로 초기화
    N = len(nums)       # 연구실 내 pokemon 수
    pokemon_nums = list(set(nums))  # pokemon 종류 list로 변환
    
    for pokemon in pokemon_nums:
        pokemon_cnt += 1    
        if pokemon_cnt == N // 2:   # 가져갈 수 있는 pokemon 수가 N/2 마리와 같아진다면,
            break
            
    return pokemon_cnt