def solution(triangle):
    max_triangle = [triangle[0]]

    for floor in range(1, len(triangle)):
        row = triangle[floor]
        temp = []
        for i, v in enumerate(row):
            if i == 0:
                temp.append(v + max_triangle[floor-1][0])

            elif i == len(row) - 1:
                temp.append(v + max_triangle[floor-1][-1])

            else:
                temp.append(max(v + max_triangle[floor-1][i-1], v + max_triangle[floor-1][i]))
        max_triangle.append(temp)
    return max(max_triangle[-1])