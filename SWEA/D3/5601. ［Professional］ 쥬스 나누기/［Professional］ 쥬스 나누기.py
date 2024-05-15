T = int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = ""
    answer += f"1/{N} " * N
    print(f"#{tc} {answer}")