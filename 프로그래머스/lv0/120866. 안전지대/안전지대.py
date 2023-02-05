def solution(board):
    answer = 0
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                for i in range(max(row-1,0), min(row+2,len(board))):
                    for j in range(max(col-1,0), min(col+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for k in board:
        answer += k.count(0)
    return answer