def zero_finder(numbers:list) -> list:
    nums = [int(index) for index in numbers]
    non_zero = [index for index in nums if index != 0]
    zeros = [index for index in nums if index == 0]
    return non_zero + zeros


number_as_string = input().split(", ")
result = zero_finder(number_as_string)
print(result)
