import constants


def lawn_x(x):
    right_x = 248 + constants.CELL_WIDTH
    column = 1
    while right_x <= x:
        right_x += constants.CELL_WIDTH
        column += 1
    center_x = right_x - constants.CELL_WIDTH / 2
    return center_x, column


def lawn_y(y):
    top_y = 24 + constants.CELL_HEIGHT
    row = 1
    while top_y <= y:
        top_y += constants.CELL_HEIGHT
        row += 1
    center_y = top_y - constants.CELL_HEIGHT / 2
    return center_y, row
