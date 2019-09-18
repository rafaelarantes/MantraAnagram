from abc import ABC, abstractmethod
from random import shuffle

class AbstractPhoneme(ABC):

    def __init__(self, letters, next_phoneme = None):
        self.next_phoneme = next_phoneme
        self._setProperties(letters) 
        self.value = self.__getFirstRandomFromList(letters)
        
        if self.next_phoneme is not None:
            self.next_phoneme = self.next_phoneme(letters)

    @abstractmethod
    def _setProperties(self, letters):
        pass

    def addToList(self, phonemes):
        if self.value != '':
            self._add(phonemes)

        if self.next_phoneme is not None:
            self.next_phoneme._add(phonemes)
    
    @abstractmethod
    def _add(self, phonemes):
        pass

    def __getFirstRandomFromList(self, letters):
        if len(letters) > 0:
            shuffle(letters)
        
            phonemes_from_list = self._getFromList(letters)
            if len(phonemes_from_list) > 0:
                for l in list(phonemes_from_list[0]):
                    letters.remove(l)

                return phonemes_from_list[0]

        return ""

    @abstractmethod
    def _getFromList(self, phonemes):
        pass

    def getValue(self):
        return self.value