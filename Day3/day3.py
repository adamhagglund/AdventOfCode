import misc.Scanner as sc

def calculate_trees(nbr_steps, nbr_down):
    map = sc.read_and_split_lines("input.txt")
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




if __name__ == "__main__":
    nbr_1 = calculate_trees(3, 1)
    nbr_2 = (calculate_trees(1, 1) * calculate_trees(3, 1) * calculate_trees(5, 1) * calculate_trees(7, 1)
           * calculate_trees(1, 2))

    print("1. ", nbr_1, "\n2. ", nbr_2)