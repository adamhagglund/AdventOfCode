def read_and_split(input, split):
    file = open(input, "r")
    words = file.read().split(split)
    file.close()
    return words

def read_and_split_lines(input):
    file = open(input, "r")
    words = file.read().splitlines()
    file.close()
    return words