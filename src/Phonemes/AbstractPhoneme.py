from abc import ABC, abstractmethod
from random import shuffle

class AbstractPhoneme(ABC):

    def __init__(self, value, next_phoneme = None):
        self.value = value
        self.next_phoneme = next_phoneme

    @abstractmethod
    def addToList(self, phonemes):
        pass

    def getFirstRandomFromList(self, phonemes):
        if len(phonemes) > 0:
            shuffle(phonemes)
        
        phonemes_from_list = __getFromList(phonemes)
        if len(phonemes_from_list) > 0:
            phonemes.remove(phonemes.index(phonemes_from_list[0]))
            return phonemes_from_list[0]

        return ""

    abstractmethod
    def __getFromList(self, phonemes):
        pass