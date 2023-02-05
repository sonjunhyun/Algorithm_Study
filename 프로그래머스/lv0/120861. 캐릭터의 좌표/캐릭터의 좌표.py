def solution(keyinput, board):
    x = 0
    y = 0
    max_x, max_y = board[0]//2, board[1]//2
    for key in keyinput:
        if key == 'left':
            if x == -max_x:
                pass
            else:
                x -= 1
        elif key == 'right':
            if x == max_x:
                pass
            else:
                x += 1
        elif key == 'up':
            if y == max_y:
                pass
            else:
                y += 1
        else:
            if y == -max_y:
                pass
            else:
                y -= 1
    return [x, y]