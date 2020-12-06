
def highest_seat():
    map = read_file("input.txt")
    rows = 127
    seats = 7
    dict = {}
    id = []

    for line in map:
        row = choose_row(line, 0, rows)
        seat = choose_seat(line[7:], 0, seats)
        dict[line] = [row, seat, row * 8 + seat]
        id.append(row * 8 + seat)

    id.sort()
    missing_id = find_missing_id(id)
    print(missing_id)
    for value in dict.values():
        if value[2] == missing_id -1 or value[2] == missing_id + 1:
            print(value)



    #print(map)
    return max(id)


def choose_row(seq, lower, upper):

    if len(seq) == 4 and seq[0] == 'F':
        return lower
    elif len(seq) == 4 and seq[0] == 'B':
        return upper

    elif seq[0] == 'F':
        return choose_row(seq[1:], lower, lower + int((upper - lower) / 2))

    elif seq[0] == 'B':
        return choose_row(seq[1:], lower + round((upper - lower) / 2), upper)

def choose_seat(seq, lower, upper):

    if len(seq) == 1 and seq[0] == 'L':
        return lower
    elif len(seq) == 1 and seq[0] == 'R':

        return upper

    elif seq[0] == 'L':

        return choose_seat(seq[1:], lower, lower + int((upper - lower) / 2))

    elif seq[0] == 'R':

        return choose_seat(seq[1:], lower + round((upper - lower) / 2), upper)


def find_missing_id(ids):
    latest = ids[0]

    for id in ids:
        if id - latest > 1:
            return(latest + 1)

        latest = id

def read_file(file_name):
    file = open(file_name, "r") #opens the file in read mode
    words = file.read().splitlines() #puts the file into an array
    file.close()
    return words

if __name__ == "__main__":
    nbr = highest_seat()
    print(nbr)