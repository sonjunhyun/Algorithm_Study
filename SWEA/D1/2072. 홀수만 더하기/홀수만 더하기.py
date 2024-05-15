for i in range(1, int(input())+1):
    #nums = [int(x) for x in input().split()]
    nums = map(int, input().split())
    answer = 0
    
    for num in nums:
        answer += num if num % 2 == 1 else 0
    print(f"#{i} {answer}")