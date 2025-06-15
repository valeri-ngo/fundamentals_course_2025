def decipher_this(word:str) -> None:
    word_input = word.split(" ")
    for word in word_input:
        number_as_string = ""
        for character in word:
            if character.isdigit():
                number_as_string += character
            else:
                break
        ascii_char = chr(int(number_as_string))
        rest_of_the_word = word[len(number_as_string):]

        if len(rest_of_the_word) > 1:
            rest_of_words = list(rest_of_the_word)
            rest_of_words[0], rest_of_words[-1] = rest_of_words[-1], rest_of_words[0]
            rest_of_the_word = "".join(rest_of_words)
        print(ascii_char + rest_of_the_word, end=" ")

text = input()
decipher_this(text)