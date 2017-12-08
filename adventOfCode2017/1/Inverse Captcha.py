from adventOfCode2017.common.Utils import readInput

inputString = readInput("input.txt")

lastChar = inputString[len(inputString) - 1]
result = 0

for char in inputString:
    if char == lastChar:
        result = result + int(char)
    lastChar = char

print("Part One: " + str(result))

print("Part Two: " + str(result))
