from collections import OrderedDict
from random import shuffle

class MantraAnagram:
    def __getVowels(self, letters):
        return list(filter(lambda x : x in ['a', 'e', 'i', 'o', 'u'], letters))

    def __getConsonants(self, letters):
        return list(filter(lambda x : x not in ['a', 'e', 'i', 'o', 'u', 'r', 's'], letters))


    def __getEndingConsonants(self, letters):
        return list(filter(lambda x : x in ['r', 's'], letters))

    def __getDigraphs(self, letters):
        digraphs = []
        for digraph in ['ch', 'lh', 'nh', 'gu', 'qu', 'sc', 'sç', 'xc', 'xs']:
            lettersDigraph = list(digraph)
            
            if lettersDigraph[0] in letters and lettersDigraph[1] in letters and len(list(filter(lambda x : lettersDigraph[0] not in list(x) or lettersDigraph[1] not in list(x), digraphs))) == 0:
                digraphs.append(digraph)
                
        return digraphs

    def __removeLetters(self, lettersForRemover, letters):
        for letter in lettersForRemover:
            if letter in letters:
                if letter in letters:  
                    letters.remove(letter)
            elif len(letter) > 1:
                for l in list(letter):
                    if l in letters:
                        letters.remove(l)

        return letters
    
    def generate(self, phrase):
        phrase = phrase.lower().replace(" ", "")
        phrase = "".join(OrderedDict.fromkeys(phrase))
        letters = list(phrase)
        shuffle(letters)

        digraphs = self.__getDigraphs(letters)
        self.__removeLetters(digraphs, letters)

        ending_consonants = self.__getEndingConsonants(letters)
        letters = self.__removeLetters(ending_consonants, letters)

        consonants = self.__getConsonants(letters)
        letters = self.__removeLetters(consonants, letters)

        vowels = self.__getVowels(letters)
        letters = self.__removeLetters(vowels, letters)
        
        final_letters = []

        while(len(digraphs) > 0 or len(consonants) > 0):
            if len(digraphs) > 0:
                final_letters.append(digraphs[0])
                digraphs = self.__removeLetters([digraphs[0]], digraphs)

                if len(vowels) > 0:
                    final_letters.append(vowels[0])
                    vowels = self.__removeLetters([vowels[0]], vowels)

            elif len(consonants) > 0:
                final_letters.append(consonants[0])
                consonants = self.__removeLetters([consonants[0]], consonants)

                if len(vowels) > 0:
                    final_letters.append(vowels[0])
                    vowels = self.__removeLetters([vowels[0]], vowels)


        if len(ending_consonants) > 0:
            while len(ending_consonants) > 0:
                final_letters.append(ending_consonants[0])
                ending_consonants = self.__removeLetters([ending_consonants[0]], ending_consonants)     

        if len(vowels) > 0:
            while len(vowels) > 0:
                if final_letters[len(final_letters)-1] in ['a', 'e', 'i', 'o', 'u']:
                    final_letters.insert(0, vowels[0])
                    vowels = self.__removeLetters([vowels[0]], vowels)
                else:
                    final_letters.append(vowels[0])
                    vowels = self.__removeLetters([vowels[0]], vowels)           

        return ''.join(final_letters)




