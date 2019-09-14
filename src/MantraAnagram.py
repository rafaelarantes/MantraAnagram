from random import shuffle
from .TextUtils import TextUtils
from .Phonemes import Phonemes

class MantraAnagram:
    def generate(self, phrase):
        phrase = TextUtils.RemoveSpecialCharacters(phrase)
        phrase = TextUtils.RemoveDuplicateCharacters(phrase)

        letters = list(phrase)
        shuffle(letters)
        final_letters = []
        phonemes = Phonemes()

        consonants, digraphs, ending_consonants, vowels = phonemes.getPhonemes(letters)
        digraphs, consonants, vowels = phonemes.addDigraphConsonantVowel(digraphs, consonants, vowels, final_letters)
        phonemes.addEndConsonants(ending_consonants, final_letters)
        phonemes.addRemainingVowels(vowels, final_letters)
        
        return ''.join(final_letters)




