from Phonemes.AbstractPhoneme import AbstractPhoneme

class Vowel(AbstractPhoneme):

    def setProperties(self, letters):
        self.next_phoneme = None

    def add(self, phonemes):
        if self.__lastElementOfListIsVowel(phonemes) and len(list(filter(lambda x : x not in ['a', 'e', 'i', 'o', 'u'], phonemes))) == 0:
            phonemes.insert(0, self.value)
        else:
            phonemes.append(self.value)

    def getFromList(self, phonemes):
        return list(filter(lambda x : x in ['a', 'e', 'i', 'o', 'u'], phonemes))

    def __lastElementOfListIsVowel(self, letters):
        if len(letters) > 0:
            return letters[len(letters)-1] in ['a', 'e', 'i', 'o', 'u']
        
        return False