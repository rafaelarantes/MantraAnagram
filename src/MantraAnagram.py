from random import shuffle
from TextUtils import TextUtils

class MantraAnagram:

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
    
    def __getPhonemes(self, letters):
        digraphs = self.__getDigraphs(letters)
        self.__removeLetters(digraphs, letters)
        
        ending_consonants = self.__getEndingConsonants(letters)
        letters = self.__removeLetters(ending_consonants, letters)
        
        consonants = self.__getConsonants(letters)
        letters = self.__removeLetters(consonants, letters)
        
        vowels = self.__getVowels(letters)
        letters = self.__removeLetters(vowels, letters)

        return consonants, digraphs, ending_consonants, vowels

    def __moveFirstLetterPhonemeForList(self, phonemes, letters):
        if len(phonemes) > 0:
            letters.append(phonemes[0])
            phonemes = self.__removeLetters([phonemes[0]], phonemes)
        return phonemes

    def __moveFirstLetterPhonemeForListByIndex(self, phonemes, letters, index):
        if len(phonemes) > 0:
            letters.insert(index, phonemes[0])
            phonemes = self.__removeLetters([phonemes[0]], phonemes)

        return phonemes


    def __getFirstUnsedVowelInList(self, vowelsNotUsedYet, letters):
        for vowel in range(0, len(vowelsNotUsedYet)):
            if vowelsNotUsedYet[vowel] in letters and letters.index(vowelsNotUsedYet[vowel]) < len(letters):
                return vowel
        
        return None

    def generate(self, phrase):
        phrase = TextUtils.RemoveSpecialCharacters(phrase)
        phrase = TextUtils.RemoveDuplicateCharacters(phrase)

        letters = list(phrase)
        shuffle(letters)

        consonants, digraphs, ending_consonants, vowels = self.__getPhonemes(letters)
        
        final_letters = []
        vowelsNotYetFound = ['a', 'e', 'i', 'o', 'u']
        consonants_first = True

        while(len(digraphs) > 0 or len(consonants) > 0):
            if not consonants_first and len(digraphs) > 0:
                digraphs = self.__moveFirstLetterPhonemeForList(digraphs, final_letters)
                vowels = self.__moveFirstLetterPhonemeForList(vowels, final_letters)

            elif len(consonants) > 0:
                if len(vowels) > 0:
                    consonants = self.__moveFirstLetterPhonemeForList(consonants, final_letters)
                else:
                    vowelNotUsedYet = self.__getFirstUnsedVowelInList(vowelsNotYetFound, final_letters)
                    
                    if vowelNotUsedYet is not None:
                        self.__moveFirstLetterPhonemeForListByIndex(consonants, final_letters, final_letters.index(vowelsNotYetFound[vowelNotUsedYet])+1)
                        vowelsNotYetFound.remove(vowelsNotYetFound[vowelNotUsedYet])
                    else:
                        consonants = self.__moveFirstLetterPhonemeForList(consonants, final_letters)

                if len(vowels) > 0:
                    vowels = self.__moveFirstLetterPhonemeForList(vowels, final_letters)
            
            consonants_first = False

        vowelsNotYetFound = ['a', 'e', 'i', 'o', 'u']
        if len(ending_consonants) > 0:
            while len(ending_consonants) > 0:
                if final_letters[len(final_letters)-1] not in ['a', 'e', 'i', 'o', 'u'] and len([i for i in vowelsNotYetFound if i in final_letters]) > 0:
                    v =  [i for i in vowelsNotYetFound if i in final_letters][0]
                    index  = final_letters.index(v)
                    final_letters.insert(index+1, ending_consonants[0])
                    ending_consonants = self.__removeLetters([ending_consonants[0]], ending_consonants)  
                    vowelsNotYetFound.remove(v) 
                else:
                    final_letters.append(ending_consonants[0])
                    ending_consonants = self.__removeLetters([ending_consonants[0]], ending_consonants)     

        if len(vowels) > 0:
            while len(vowels) > 0:
                if len(final_letters) > 0 and final_letters[len(final_letters)-1] in ['a', 'e', 'i', 'o', 'u']:
                    final_letters.insert(0, vowels[0])
                    vowels = self.__removeLetters([vowels[0]], vowels)
                else:
                    vowels = self.__moveFirstLetterPhonemeForList(vowels, final_letters)

        return ''.join(final_letters)




