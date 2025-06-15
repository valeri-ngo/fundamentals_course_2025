def which_are_in(first:str, second:str) -> list:
    filtered_sequence = []

    for current_sentence in first.split(', '):
        current_sentence_lower = current_sentence.lower()
        for word in second.split(', '):
            if current_sentence_lower in word.lower():
                filtered_sequence.append(current_sentence)
                break

    return filtered_sequence

first_sequence = input()
second_sequence = input()
result = which_are_in(first_sequence, second_sequence)
print(result)