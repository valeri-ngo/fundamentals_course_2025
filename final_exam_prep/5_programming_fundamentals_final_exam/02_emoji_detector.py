import re


class Emoji:

    def __init__(self):
        pass

    def regex(self, string):
        self.key = r'(\*\*|::)([A-Z][a-z]{2,})\1'
        string = list(re.finditer(self.key, string))
        return string

    def cool_threshold(self, string):
        cool_threshold = 1
        for digit in re.findall(r'\d', string):
            cool_threshold *= int(digit)
        return cool_threshold

    def sum_emojis(self, matches, threshold):
        cool_emojis = []
        for match in matches:
            emoji_word = match.group(2)
            coolness = sum(ord(ch) for ch in emoji_word)
            if coolness >= threshold:
                cool_emojis.append(match.group(0))
        return cool_emojis

    def main(self):

        string = input()

        matches = self.regex(string)
        threshold = self.cool_threshold(string)
        cool_emojis = self.sum_emojis(matches, threshold)

        print(f"Cool threshold: {threshold}")
        print(f"{len(matches)} emojis found in the text. The cool ones are:")
        for emoji in cool_emojis:
            print(emoji)

if __name__ == '__main__':
    emoji_detector = Emoji()
    emoji_detector.main()