from Phonemes.AbstractPhoneme import AbstractPhoneme

class Suffix(AbstractPhoneme):

    def addToList(self, phonemes):
        phonemes.append(self.value)

    def getFromList(self, phonemes):
        return list(filter(lambda x : x in ['r', 's'], phonemes))
