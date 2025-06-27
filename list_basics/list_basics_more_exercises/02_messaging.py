numbers_as_string = input()
some_text = input()

numbers_as_list = numbers_as_string.split()
number_as_integer = [int(num) for num in numbers_as_list]
text = list(some_text)
message = ""

for number in number_as_integer:
    index = sum(int(digit) for digit in str(number))
    index = index % len(text)
    message += text[index]
    text.pop(index)

print(message)