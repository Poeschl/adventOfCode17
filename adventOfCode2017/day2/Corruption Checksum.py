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


def getEvenNumbersDiff(line: str):
    numbers = line.split(" ")

    for index1, first_num in enumerate(numbers):
        first_num = int(first_num)
        for index2, second_num in enumerate(numbers):
            second_num = int(second_num)
            if first_num % second_num == 0 and first_num > second_num and index1 != index2:
                return int(first_num / second_num)


puzzleInput = readInputLines("input.txt")
checksum = 0
even_checksum = 0

for line in puzzleInput:
    checksum = checksum + getDiffOfMinAndMax(line)
    even_checksum = even_checksum + getEvenNumbersDiff(line)

printOutput(checksum, even_checksum)
