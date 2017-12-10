def readInput(file):
    return readInputLines(file)[0]


def printOutput(resutl1, result2):
    print("Part One: " + str(resutl1))
    print("Part Two: " + str(result2))


def readInputLines(file):
    with open(file) as f:
        content = f.readlines()
    return [line.strip() for line in content]
