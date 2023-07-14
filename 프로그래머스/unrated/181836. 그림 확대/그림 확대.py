def solution(picture, k):
    result = []

    # 픽셀을 k배 확장한 그림 파일 생성
    for row in picture:
        new_row = ''
        for pixel in row:
            new_row += pixel * k
        result.extend([new_row] * k)

    return result