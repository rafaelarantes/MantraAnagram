from random import shuffle
from TextUtils import TextUtils
from PhonemesFactory import PhonemesFactory

class MantraAnagram:
    def generate(self, phrase):
        phrase = TextUtils.RemoveSpecialCharacters(phrase)
        phrase = TextUtils.RemoveDuplicateCharacters(phrase)

        letters = list(phrase)
        shuffle(letters)
        final_letters = []
        phonemes = PhonemesFactory()

        phonemes.addPhonemes(final_letters, letters)
        return ''.join(final_letters)




