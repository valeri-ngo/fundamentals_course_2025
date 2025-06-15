numbers = input().split(', ')
number = [int(num) for num in numbers]
odd_list = [num for num in number if num % 2 != 0]
even_list = [num for num in number if num % 2 == 0]
positive_list = [num for num in number if int(num) >= 0]
negative_list = [num for num in number if (int(num) < 0)]

print(f"Positive: {', '.join(str(num) for num in positive_list)}")
print(f"Negative: {', '.join(str(num) for num in negative_list)}")
print(f"Even: {', '.join(str(num) for num in even_list)}")
print(f"Odd: {', '.join(str(num) for num in odd_list)}")