from random import shuffle
from Phonemes.Consonant import Consonant
from Phonemes.Digraph import Digraph
from Phonemes.Vowel import Vowel
from Phonemes.Suffix import Suffix

phonemes_names = [Consonant.__name__, Digraph.__name__, Suffix.__name__, Vowel.__name__]
class PhonemesFactory:

    def addPhonemes(self, diagram_letters, phrase_letters):
        while len(phrase_letters) > 0:
            shuffle(phonemes_names)
            for phoneme_name in phonemes_names:
                self.__addPhonemeToList(phoneme_name, diagram_letters, phrase_letters, Vowel.__name__)


    def __addPhonemeToList(self, phoneme_name, diagram_letters, phrase_letters, next_phoneme_name = None):
        next_phoneme = None
        phoneme_class = globals()[phoneme_name]

        if next_phoneme_name is not None:
            next_phoneme = globals()[next_phoneme_name]

        phoneme = phoneme_class(phrase_letters, next_phoneme)
        phoneme.addToList(diagram_letters)
