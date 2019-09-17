from Phonemes.AbstractPhoneme import AbstractPhoneme

class Vowel(AbstractPhoneme):

    def addToList(self, phonemes):
        phonemes.append(self.value)

    def getFromList(self, phonemes):
        return list(filter(lambda x : x in ['a', 'e', 'i', 'o', 'u'], phonemes))
