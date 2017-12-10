from adventOfCode2017.common.Utils import readInput, printOutput

inputString = readInput("input.txt")

lastChar = inputString[len(inputString) - 1]
matches = 0
extendedMatches = 0
halfway = int(len(inputString) / 2)

for index, char in enumerate(inputString):
    if char == lastChar:
        matches = matches + int(char)

    if char == inputString[(index + halfway) % len(inputString)]:
        extendedMatches = extendedMatches + int(char)

    lastChar = char

printOutput(matches, extendedMatches)
