from Phonemes.AbstractPhoneme import AbstractPhoneme

class Suffix(AbstractPhoneme):

    def setProperties(self, letters):
        self.next_phoneme = None

    def add(self, phonemes):
        phonemes.append(self.value)

    def getFromList(self, phonemes):
        if len(list(filter(lambda x : x not in ['r', 's'], phonemes))) == 0:
            return list(filter(lambda x : x in ['r', 's'], phonemes))

        return []
