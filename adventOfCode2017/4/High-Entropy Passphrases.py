from adventOfCode2017.common.Utils import readInputLines, printOutput


class Word:
    data: str
    charDict: dict

    def __init__(self, data):
        self.data = data

        for character in data:
            if self.charDict[character] != "":
                self.charDict[character] = self.charDict[character] + 1
            else:
                self.charDict[character] = 1

    def is_a_anagram_of(self, other: Word):
        for character in self.charDict:

        return False

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return self.data == o.data
        else:
            return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)


def pass_is_compliant(passline: str):
    known_words = []
    words = passline.split(" ")
    for word in words:
        password = Word(word)
        if password in known_words:
            return False
        else:
            known_words.append(password)
    return True


def pass_is_anagram_compliant(passline: str):
    known_words = []
    words = []
    for text in passLine.split(" "):
        words.append(Word(text))

    for currentWord in words:
        for storedWord in known_words:
            if currentWord.is_a_anagram_of(storedWord):
                return False
            else:
                known_words.append(currentWord)
    return True


puzzleInput = readInputLines("test.txt")
correctPasses = 0
correctAnagramPasses = 0

for passLine in puzzleInput:
    if pass_is_compliant(passLine):
        correctPasses = correctPasses + 1
    if pass_is_anagram_compliant(passLine):
        correctAnagramPasses = correctAnagramPasses + 1

printOutput(correctPasses, 0)
