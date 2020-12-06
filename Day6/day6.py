
def highest_seat():
    map = read_file("input.txt")
    groups = []
    for group in map:
        groups.append(group.split("\n"))

    score_dict = {}

    for i, group in enumerate(groups):
        yes_array = []
        check_array = []
        print(group)
        for char in group[0]:
            yes_array.append(char)
            check_array.append(char)

        for char in check_array:
            for y in range(1, len(group)):

                print(char, yes_array)
                if char not in group[y] and char in yes_array:
                    yes_array.remove(char)




        print(yes_array)
        score_dict[i] = yes_array

    sum_a = 0
    for value in score_dict.values():
        sum_a = sum_a + len(value)


    return sum_a


def choose_row(seq, lower, upper):
    return None


def choose_seat(seq, lower, upper):

    return None



def find_missing_id(ids):
    latest = ids[0]

    for id in ids:
        if id - latest > 1:
            return(latest + 1)

        latest = id

def read_file(file_name):
    file = open(file_name, "r") #opens the file in read mode
    words = file.read().split("\n\n") #puts the file into an array

    file.close()
    return words

if __name__ == "__main__":
    nbr = highest_seat()
    print(nbr)