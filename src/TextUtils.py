from unicodedata import normalize
from re import sub
from collections import OrderedDict

class TextUtils:
    @staticmethod
    def RemoveSpecialCharacters(text):
        text = text.lower().replace(" ", "")
        text = str(normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8"))
        text = sub('[^a-z]+', '', text)
        return text

    @staticmethod
    def RemoveDuplicateCharacters(text):
        return "".join(OrderedDict.fromkeys(text))

    
