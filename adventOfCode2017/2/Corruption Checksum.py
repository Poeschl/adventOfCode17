import sys

from adventOfCode2017.common.Utils import readInputLines, printOutput


def getDiffOfMinAndMax(line: str):
    numbers = line.split(" ")
    min_number = sys.maxsize
    max_number = -sys.maxsize

    for number in numbers:
        number = int(number)
        if number < min_number:
            min_number = number

        if number > max_number:
            max_number = number

    return max_number - min_number


puzzleInput = readInputLines("input.txt")
checksum = 0

for line in puzzleInput:
    checksum = checksum + getDiffOfMinAndMax(line)

printOutput(checksum, 0)
