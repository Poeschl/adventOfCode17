from adventOfCode2017.common.Utils import readInputLines, printOutput
from adventOfCode2017.day4.Word import Word


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
    words = []
    for text in passline.split(" "):
        words.append(Word(text))

    for currentIndex, currentWord in enumerate(words):
        for storedIndex, storedWord in enumerate(words):
            if currentIndex != storedIndex and currentWord.is_a_anagram_of(storedWord):
                return False
    return True


puzzleInput = readInputLines("input.txt")
correctPasses = 0
correctAnagramPasses = 0

for passLine in puzzleInput:
    if pass_is_compliant(passLine):
        correctPasses = correctPasses + 1
    if pass_is_anagram_compliant(passLine):
        correctAnagramPasses = correctAnagramPasses + 1

printOutput(correctPasses, correctAnagramPasses)
