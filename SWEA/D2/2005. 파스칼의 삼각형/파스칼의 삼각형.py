for test_case in range(1, int(input())+1):
    N = int(input())
    print(f"#{test_case}")
    pascal = [[0] * N for _ in range(N)]
    pascal[0][0] = 1

    for i in range(1, N):
        for j in range(N):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    
    for k in range(N):
        for l in range(N):
            if pascal[k][l]:
                print(pascal[k][l], end=" ")
        print()