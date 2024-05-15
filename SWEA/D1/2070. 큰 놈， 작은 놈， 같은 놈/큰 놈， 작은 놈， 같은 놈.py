for i in range(1, int(input())+1):
    #nums = list(map(int, input().split()))
    nums = [int(num) for num in input().split()]
    answer = '>' if nums[0] > nums[1] else '<' if nums[0] < nums[1] else '='
    print(f"#{i} {answer}")