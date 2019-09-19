from abc import ABC, abstractmethod
from random import shuffle

class AbstractPhoneme(ABC):

    def __init__(self, phrase_letters, next_phoneme = None):
        self.next_phoneme = next_phoneme
        self._setProperties(phrase_letters) 
        self.value = self.__getFirstRandomFromList(phrase_letters)
        
        if self.next_phoneme is not None:
            self.next_phoneme = self.next_phoneme(phrase_letters)

    @abstractmethod
    def _setProperties(self, phrase_letters):
        pass

    def addToList(self, diagram_letters):
        if self.value != '':
            self._add(diagram_letters)

        if self.next_phoneme is not None:
            self.next_phoneme._add(diagram_letters)
    
    @abstractmethod
    def _add(self, diagram_letters):
        pass

    def __getFirstRandomFromList(self, phrase_letters):
        if len(phrase_letters) > 0:
            shuffle(phrase_letters)
        
            phonemes_from_list = self._getFromList(phrase_letters)
            if len(phonemes_from_list) > 0:
                for l in list(phonemes_from_list[0]):
                    phrase_letters.remove(l)

                return phonemes_from_list[0]

        return ""

    @abstractmethod
    def _getFromList(self, phrase_letters):
        pass

    def getValue(self):
        return self.value