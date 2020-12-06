
def calculate_trees(nbr_down, nbr_steps):
    map = read_file("input.txt")
    dict = {}
    key = 1
    nbr = nbr_steps

    for line in map:
        dict[key] = line

        while len(dict[key]) <= nbr*len(map):
            dict[key] = dict[key] + dict[key]

        key = key + 1

    position = nbr
    amount = 0

    for x in range(2, len(map) + 1):

        if x % nbr_down != 0 or nbr_down == 1:
            row = dict[x]
            if row[position] == '.':
                temp_row = row[:position] + 'O' + row[position + 1:]
                dict[x] = temp_row
            elif row[position] == '#':
                temp_row = row[:position] + 'X' + row[position + 1:]
                dict[x] = temp_row

                amount = amount + 1

            position = position + nbr

    return(amount)



def read_file(file_name):
    file = open(file_name, "r") #opens the file in read mode
    words = file.read().splitlines() #puts the file into an array
    file.close()
    return words

if __name__ == "__main__":
    nbr = calculate_trees(1, 1)
    print(nbr)
    print(94 * 214 * 99 * 91 * 46)