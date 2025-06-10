from colorama import Fore, Style, init
import sys

init(autoreset=True)

def right_angled_triangle(rows):
    for i in range(1, rows + 1):
        print(Fore.GREEN + "*" * i)

def square_with_hollow_center(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print(Fore.BLUE + "*" * size)
        else:
            print(Fore.BLUE + "*" + " " * (size - 2) + "*")

def diamond(rows):
    for i in range(rows):
        print(Fore.MAGENTA + " " * (rows - i - 1) + "*" * (2 * i + 1))
    for i in range(rows - 2, -1, -1):
        print(Fore.MAGENTA + " " * (rows - i - 1) + "*" * (2 * i + 1))

def left_angled_triangle(rows):
    for i in range(1, rows + 1):
        print(Fore.CYAN + " " * (rows - i) + "*" * i)

def hollow_square(size):
    square_with_hollow_center(size)

def pyramid(rows):
    for i in range(rows):
        print(Fore.YELLOW + " " * (rows - i - 1) + "*" * (2 * i + 1))

def reverse_pyramid(rows):
    for i in range(rows):
        print(Fore.RED + " " * i + "*" * (2 * (rows - i) - 1))

def rectangle_with_hollow_center(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print(Fore.BLUE + "*" * width)
        else:
            print(Fore.BLUE + "*" + " " * (width - 2) + "*")

def spiral_pattern(n):
    mat = [[" " for _ in range(n)] for _ in range(n)]
    left, right, top, bottom = 0, n-1, 0, n-1
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            mat[top][i] = "*"
        top += 1
        for i in range(top, bottom+1):
            mat[i][right] = "*"
        right -= 1
        for i in range(right, left-1, -1):
            mat[bottom][i] = "*"
        bottom -= 1
        for i in range(bottom, top-1, -1):
            mat[i][left] = "*"
        left += 1
    for row in mat:
        print(Fore.WHITE + "".join(row))

def checkerboard_pattern(n):
    for i in range(n):
        for j in range(n):
            print(Fore.LIGHTWHITE_EX + ("*" if (i + j) % 2 == 0 else " "), end="")
        print()

def alphabet_pyramid(rows):
    for i in range(rows):
        print(Fore.LIGHTBLUE_EX + chr(65 + i) * (i + 1))

def save_pattern_to_file(filename, pattern_function, *args):
    original_stdout = sys.stdout
    with open(filename, 'w') as f:
        sys.stdout = f
        pattern_function(*args)
    sys.stdout = original_stdout
    print(f"✅ Pattern saved to {filename}\n")

def main():
    print("\n🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Spiral")
    print("10. Checkerboard")
    print("11. Alphabet Pyramid")

    # Predefined test values to bypass input in sandboxed environment
    test_inputs = {
        'choice': 1,
        'rows': 5,
        'size': 5,
        'width': 10,
        'height': 4,
        'save': 'n',
        'filename': 'pattern.txt'
    }

    choice = test_inputs['choice']

    if choice in [1, 3, 4, 6, 7, 11]:
        rows = test_inputs['rows']
    elif choice in [2, 5, 9, 10]:
        size = test_inputs['size']
    elif choice == 8:
        width = test_inputs['width']
        height = test_inputs['height']

    print("\n✨ Your Pattern:")

    if choice == 1:
        right_angled_triangle(rows)
    elif choice == 2:
        square_with_hollow_center(size)
    elif choice == 3:
        diamond(rows)
    elif choice == 4:
        left_angled_triangle(rows)
    elif choice == 5:
        hollow_square(size)
    elif choice == 6:
        pyramid(rows)
    elif choice == 7:
        reverse_pyramid(rows)
    elif choice == 8:
        rectangle_with_hollow_center(width, height)
    elif choice == 9:
        spiral_pattern(size)
    elif choice == 10:
        checkerboard_pattern(size)
    elif choice == 11:
        alphabet_pyramid(rows)
    else:
        print("❌ Invalid choice!")
        return

    if test_inputs['save'] == 'y':
        filename = test_inputs['filename']
        if choice == 1:
            save_pattern_to_file(filename, right_angled_triangle, rows)
        elif choice == 2:
            save_pattern_to_file(filename, square_with_hollow_center, size)
        elif choice == 3:
            save_pattern_to_file(filename, diamond, rows)
        elif choice == 4:
            save_pattern_to_file(filename, left_angled_triangle, rows)
        elif choice == 5:
            save_pattern_to_file(filename, hollow_square, size)
        elif choice == 6:
            save_pattern_to_file(filename, pyramid, rows)
        elif choice == 7:
            save_pattern_to_file(filename, reverse_pyramid, rows)
        elif choice == 8:
            save_pattern_to_file(filename, rectangle_with_hollow_center, width, height)
        elif choice == 9:
            save_pattern_to_file(filename, spiral_pattern, size)
        elif choice == 10:
            save_pattern_to_file(filename, checkerboard_pattern, size)
        elif choice == 11:
            save_pattern_to_file(filename, alphabet_pyramid, rows)

    print("\n🎉 Done! Thank you for using the Pattern Drawing Program.")

if __name__ == "__main__":
    main()
