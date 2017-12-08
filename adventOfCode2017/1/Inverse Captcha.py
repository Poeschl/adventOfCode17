from adventOfCode2017.common.Utils import readInput

inputString = readInput("input.txt")

lastChar = ''
result = 0

for char in inputString:
    if char == lastChar and lastChar != '':
        result = result + int(char)
    lastChar = char

if inputString[0] == inputString[len(inputString)-1]:
    result = result + int(inputString[len(inputString)-1])

print(result)
