def check_cell(field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if field[j][i]:
                count += 1

    if field[y][x]:
        count -= 1
        if count in (2, 3):
            return 1
    else:
        if count == 3:
            return 1

        return 0
