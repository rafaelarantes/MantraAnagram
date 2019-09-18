from Phonemes.AbstractPhoneme import AbstractPhoneme

vowels = ['a', 'e', 'i', 'o', 'u']
class Vowel(AbstractPhoneme):
    
    def _setProperties(self, letters):
        self.next_phoneme = None

    def _add(self, phonemes):
        if self.__lastElementOfListIsVowel(phonemes):
            phonemes.insert(0, self.value)
        else:
            phonemes.append(self.value)

    def _getFromList(self, phonemes):
        return list(filter(lambda x : x in vowels, phonemes))

    def __lastElementOfListIsVowel(self, letters):
        if len(letters) > 0:
            return letters[len(letters)-1] in vowels
        
        return False

    @staticmethod
    def getVowels():
        return vowels