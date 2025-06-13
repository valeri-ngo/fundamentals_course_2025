from math import floor

def center_point(x1:float, y1:float, x2:float, y2:float) -> float:
    cords1 = x1 ** 2 + y1 ** 2
    cords2 = x2 ** 2 + y2 ** 2
    if cords1 < cords2:
        return x1, y1
    else:
        return x2, y2

x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())

x, y = center_point(x1_input, y1_input, x2_input, y2_input)
print(f"({floor(x)}, {floor(y)})")