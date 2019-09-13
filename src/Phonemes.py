from LetterUtils import LetterUtils

class Phonemes:
    def __getVowels(self, letters):
        return list(filter(lambda x : x in ['a', 'e', 'i', 'o', 'u'], letters))

    def __getConsonants(self, letters):
        return list(filter(lambda x : x not in ['a', 'e', 'i', 'o', 'u', 'r', 's'], letters))


    def __getEndingConsonants(self, letters):
        return list(filter(lambda x : x in ['r', 's'], letters))

    def __getDigraphs(self, letters):
        digraphs = []
        for digraph in ['ch', 'lh', 'nh', 'gu', 'qu', 'sc', 'sç', 'xc', 'xs',
                        'gh', 'th', 'sh', 'zh', 'rh', 'ph', 'wh', 'wr', 'ck',
                        'kn', 'dg', 'pn', 'ps', 'ng',
                       ]:
            lettersDigraph = list(digraph)
            
            if lettersDigraph[0] in letters and lettersDigraph[1] in letters and len(list(filter(lambda x : lettersDigraph[0] in list(x) or lettersDigraph[1] in list(x), digraphs))) == 0:
                digraphs.append(digraph)
                
        return digraphs
    
    def __moveFirstLetterPhonemeForList(self, phonemes, letters):
        if len(phonemes) > 0:
            letters.append(phonemes[0])
            phonemes = LetterUtils.removeLetters([phonemes[0]], phonemes)
        return phonemes

    def __moveFirstLetterPhonemeForListByIndex(self, phonemes, letters, index):
        if len(phonemes) > 0:
            letters.insert(index, phonemes[0])
            phonemes = LetterUtils.removeLetters([phonemes[0]], phonemes)

        return phonemes


    def __valueOfListContainsInAnotherList(self, first_list, second_list):
        return len([i for i in first_list if i in second_list]) > 0

    def __getFirstUnsedVowelInList(self, vowelsNotUsedYet, letters):
        for vowel in range(0, len(vowelsNotUsedYet)):
            if vowelsNotUsedYet[vowel] in letters and letters.index(vowelsNotUsedYet[vowel]) < len(letters):
                return vowelsNotUsedYet[vowel]
        
        return None
    
    def __lastElementOfListIsVowel(self, letters):
        return letters[len(letters)-1] in ['a', 'e', 'i', 'o', 'u']

    def getPhonemes(self, letters):
        digraphs = self.__getDigraphs(letters)
        LetterUtils.removeLetters(digraphs, letters)
        
        ending_consonants = self.__getEndingConsonants(letters)
        letters = LetterUtils.removeLetters(ending_consonants, letters)
        
        consonants = self.__getConsonants(letters)
        letters = LetterUtils.removeLetters(consonants, letters)
        
        vowels = self.__getVowels(letters)
        letters = LetterUtils.removeLetters(vowels, letters)

        return consonants, digraphs, ending_consonants, vowels
    
    def addEndConsonants(self, ending_consonants, letters):
        vowelsNotUsedYet = ['a', 'e', 'i', 'o', 'u']

        while len(ending_consonants) > 0:
            if not self.__lastElementOfListIsVowel(letters) and self.__valueOfListContainsInAnotherList(vowelsNotUsedYet, letters):
                vowelNotUsedYet = self.__getFirstUnsedVowelInList(vowelsNotUsedYet, letters)

                if vowelNotUsedYet is not None:
                    self.__moveFirstLetterPhonemeForListByIndex(ending_consonants, letters, letters.index(vowelNotUsedYet) + 1)
                    vowelsNotUsedYet.remove(vowelNotUsedYet) 
            else:
                ending_consonants = self.__moveFirstLetterPhonemeForList(ending_consonants, letters)

    def addRemainingVowels(self, vowels, letters):
        while len(vowels) > 0:
            if len(letters) > 0 and self.__lastElementOfListIsVowel(letters):
                self.__moveFirstLetterPhonemeForListByIndex(vowels, letters, 0)
            else:
                self.__moveFirstLetterPhonemeForList(vowels, letters)
    
    def addDigraph(self, digraphs, letters):
        if len(digraphs) > 0:
            digraphs = self.__moveFirstLetterPhonemeForList(digraphs, letters)
        
        return digraphs
    
    def addVowel(self, vowels, letters):
        if len(vowels) > 0:
            vowels = self.__moveFirstLetterPhonemeForList(vowels, letters)
        
        return vowels

    def addConsonant(self, consonants, letters):
        if len(consonants) > 0:
            consonants = self.__moveFirstLetterPhonemeForList(consonants, letters)
        
        return consonants
    
    def addDigraphConsonantVowel(self, digraphs, consonants, vowels, letters):
        vowelsNotUsedYet = ['a', 'e', 'i', 'o', 'u']
        consonants_first = True

        while(len(digraphs) > 0 or len(consonants) > 0):
            if not consonants_first and len(digraphs) > 0:
                digraphs = self.addDigraph(digraphs, letters)
                vowels = self.addVowel(vowels, letters)

            elif len(consonants) > 0:
                if len(vowels) > 0:
                    consonants = self.addConsonant(consonants, letters)
                else:
                    vowelNotUsedYet = self.__getFirstUnsedVowelInList(vowelsNotUsedYet, letters)
                    
                    if vowelNotUsedYet is not None:
                        self.__moveFirstLetterPhonemeForListByIndex(consonants, letters, letters.index(vowelNotUsedYet) + 1)
                        vowelsNotUsedYet.remove(vowelNotUsedYet)
                    else:
                        consonants = self.addConsonant(consonants, letters)

                if len(vowels) > 0:
                    vowels = self.addVowel(vowels, letters)
            
            consonants_first = False
        
        return digraphs, consonants, vowels