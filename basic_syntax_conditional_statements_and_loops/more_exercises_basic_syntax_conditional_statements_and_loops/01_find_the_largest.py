n = input()

for i in range(9, -1, -1):
    for number in n:
        if int(number) == i:
            print(i, end="")
