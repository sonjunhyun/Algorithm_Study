T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0]*N
    
    for i in range(N):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
            
    print(f"#{tc} {max(dp)}")