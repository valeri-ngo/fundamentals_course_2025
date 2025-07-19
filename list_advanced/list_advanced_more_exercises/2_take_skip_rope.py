def numbers_list(string_number: str) -> list[int]:
    digits = [int(char) for char in string_number if char.isdigit()]
    return digits

def non_number(non_number: str) -> list[str]:
    result = list(char for char in non_number if not char.isdigit())
    return result

def even_number_list(numbers: list[int]) -> list[int]:
    return [numbers[i] for i in range(0, len(numbers), 2)]

def odd_number_list(numbers: list[int]) -> list[int]:
    return [numbers[i] for i in range(1, len(numbers), 2)]

def take_or_skip_text(non_numbers:list[str], take:list[int], skip:list[int]) -> str:
    result = []
    current_index = 0

    for taken, skipped in zip(take,skip):
        taken_chars = non_numbers[current_index:current_index + taken]
        result.extend(taken_chars)
        current_index += taken
        current_index += skipped

        if current_index >= len(non_numbers):
            break
    return ''.join(result)

some_string = input()

numbers = numbers_list(some_string)
non_numbers = non_number(some_string)
take = even_number_list(numbers)
skip = odd_number_list(numbers)

hidden_message = take_or_skip_text(non_numbers, take, skip)

print(hidden_message)