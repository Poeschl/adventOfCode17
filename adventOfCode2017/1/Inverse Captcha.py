from adventOfCode2017.common.Utils import readInput, printOutput

inputString = readInput("input.txt")

lastChar = inputString[len(inputString) - 1]
result = 0

for char in inputString:
    if char == lastChar:
        result = result + int(char)
    lastChar = char

printOutput(result, result)
