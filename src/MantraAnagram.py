from random import shuffle
from TextUtils import TextUtils
from Phonemes.PhonemesFactory import PhonemesFactory

class MantraAnagram:
    def generate(self, phrase):
        phrase = TextUtils.RemoveSpecialCharacters(phrase)
        phrase = TextUtils.RemoveDuplicateCharacters(phrase)

        phrase_letters = list(phrase)
        shuffle(phrase_letters)
        diagram_letters = []

        self.__addPhraseLettersInDiagramLetters(phrase_letters, diagram_letters)

        return ''.join(diagram_letters)
    
    def __addPhraseLettersInDiagramLetters(self, phrase_letters, diagram_letters):
        phonemesFactory = PhonemesFactory()
        next_phoneme = phonemesFactory.getVowel()

        while len(phrase_letters) > 0:
            phonemes = phonemesFactory.getPhonemes()
            for phoneme in phonemes:
                phoneme(phrase_letters, next_phoneme).addToList(diagram_letters)



