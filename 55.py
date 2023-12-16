class Text:
    def __init__(self, text):
        self.text = text

    def count_characters(self):
        return len(self.text)

    def count_letters(self):
        letters = [char for char in self.text if char.isalpha()]
        return len(letters)

    def count_spaces(self):
        spaces = [char for char in self.text if char.isspace()]
        return len(spaces)

    def count_characters_without_spaces(self):
        characters = [char for char in self.text if not char.isspace()]
        return len(characters)

    def get_word_array(self):
        words = self.text.split()
        return words

    def get_sentence_array(self):
        # Assume sentence ends with '.', '!', or '?'
        sentences = self.text.split('. ')
        sentences = [sentence.rstrip('!') for sentence in sentences]
        return sentences
