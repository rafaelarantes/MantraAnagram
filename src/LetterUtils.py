
class LetterUtils:
    @staticmethod
    def removeLetters(lettersForRemover, letters):
        for letter in lettersForRemover:
            if letter in letters:
                letters.remove(letter)
            elif len(letter) > 1:
                for l in list(letter):
                    if l in letters:
                        letters.remove(l)

        return letters