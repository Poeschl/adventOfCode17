def readInput(file):
    with open(file) as f:
        return f.read().replace('\n', '')


def printOutput(resutl1, result2):
    print("Part One: " + str(resutl1))
    print("Part Two: " + str(result2))
