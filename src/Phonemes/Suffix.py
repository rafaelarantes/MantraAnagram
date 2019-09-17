from Phonemes.AbstractPhoneme import AbstractPhoneme

class Suffix(AbstractPhoneme):

    def setProperties(self, letters):
        pass

    def addToList(self, phonemes):
        if self.value != '':
            phonemes.append(self.value)

    def getFromList(self, phonemes):
        if len(list(filter(lambda x : x not in ['r', 's'], phonemes))) == 0:
            return list(filter(lambda x : x in ['r', 's'], phonemes))

        return []
