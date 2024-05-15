for i in range(1, int(input())+1):
    #nums = list(map(int, input().split()))
    nums = [int(x) for x in input().split()]
    answer = 0
    
    for num in nums:
        answer += num

    print(f"#{i} {round(answer / len(nums))}")