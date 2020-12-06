import misc.Scanner as scanner


def declaration_check():
    map = scanner.read_and_split("input.txt", "\n\n")
    groups = []
    for group in map:
        groups.append(group.split("\n"))

    score_dict = solve_2(groups)



    sum_a = 0
    for value in score_dict.values():
        sum_a = sum_a + len(value)

    return sum_a


def solve_1(groups):
    score_dict = {}

    for i, group in enumerate(groups):
        yes_array = []

        for entry in group:
            for char in entry:
                if char not in yes_array:
                    yes_array.append(char)

        score_dict[i] = yes_array

    return score_dict


def solve_2(groups):
    score_dict = {}
    for i, group in enumerate(groups):
        yes_array = []

        for char in group[0]:
            yes_array.append(char)

        for char in group[0]:
            for y in range(1, len(group)):
                if char not in group[y] and char in yes_array:
                    yes_array.remove(char)

        score_dict[i] = yes_array

    return score_dict

if __name__ == "__main__":
    nbr = declaration_check()
    print(nbr)