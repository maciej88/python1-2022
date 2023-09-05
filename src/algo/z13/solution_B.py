def get_area(x1, y1, x2, y2) -> int:
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1

    return width * height
