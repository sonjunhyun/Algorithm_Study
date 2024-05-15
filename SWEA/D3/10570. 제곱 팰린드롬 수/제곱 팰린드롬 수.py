T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    sq_palindrome = 0
    
    for i in range(A, B+1):
        N = str(i)
        sqrt_N = str(i**0.5).split('.0')[0]
        if N == N[::-1] and sqrt_N == sqrt_N[::-1]:
            sq_palindrome += 1
        
    print(f"#{tc} {sq_palindrome}")