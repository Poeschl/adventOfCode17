def readInput(file):
    with open(file) as f:
        return f.read().replace('\n', '')
