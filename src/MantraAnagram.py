from random import shuffle
from TextUtils import TextUtils
from PhonemesFactory import PhonemesFactory

class MantraAnagram:
    def generate(self, phrase):
        phrase = TextUtils.RemoveSpecialCharacters(phrase)
        phrase = TextUtils.RemoveDuplicateCharacters(phrase)

        phrase_letters = list(phrase)
        shuffle(phrase_letters)
        diagram_letters = []
        phonemesFactory = PhonemesFactory()

        phonemesFactory.addPhonemes(diagram_letters, phrase_letters)
        return ''.join(diagram_letters)




