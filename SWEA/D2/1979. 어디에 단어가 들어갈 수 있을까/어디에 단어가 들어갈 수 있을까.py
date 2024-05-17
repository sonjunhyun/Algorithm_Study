for i in range(1, int(input())+1):
    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]
    space_able = 0
    
    for row in puzzle:
        row_spaces = ''.join(row).split('0')
        space_able += row_spaces.count('1'*K)

    for col in zip(*puzzle):
        col_space = ''.join(col).split('0')
        space_able += col_space.count('1'*K)
               
    print(f"#{i} {space_able}")