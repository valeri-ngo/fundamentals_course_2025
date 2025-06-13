from math import floor

def line_length(x1:float, y1:float, x2:float, y2:float,
                 x3:float, y3:float, x4:float, y4:float) -> tuple:
    length1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    length2 = ((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5
    if length1 >= length2:
        return x1, y1 , x2, y2
    else:
        return x3, y3, x4, y4

def center_point(x1:float, y1:float, x2:float, y2:float) -> tuple:
    cords1 = x1 ** 2 + y1 ** 2
    cords2 = x2 ** 2 + y2 ** 2
    if cords1 <= cords2:
        return x1, y1, x2, y2
    else:
        return x2, y2, x1, y1

x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())
x3_input = float(input())
y3_input = float(input())
x4_input = float(input())
y4_input = float(input())

x1, y1, x2, y2 = line_length(x1_input, y1_input, x2_input, y2_input,
                             x3_input, y3_input, x4_input, y4_input)
x1, y1 , x2, y2 = center_point(x1, y1, x2, y2)
print(f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})")