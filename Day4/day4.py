import re

def valid_passports():
    batch = read_file("input.txt")
    must_haves = ["byr", "iyr", "eyr",
                   "hgt", "hcl", "ecl", "pid"]
    nbr_valid_pass = 0
    split1 = []
    for _ in range(0, len(batch)):
        split1.append({"byr": None, "iyr": None, "eyr": None, "hgt": None, "hcl": None,
        "ecl": None, "pid": None})



    index = 0
    for pw in batch:
        splitLine1 = re.split('\n |\s', pw)

        for line in splitLine1:
            key_value = line.split(":")
            if len(key_value) == 2:
                k_v = {line.split(":")[0]: line.split(":")[1]}

                split1[index].update(k_v)

        index = index + 1


    for passport in split1:
        OK = True
        must_temp = ["hcl"]#"ecl","hgt", "pid", "byr", "iyr", "eyr"]
        for must in must_haves:
            if passport[must] is None:
                OK = False

            else:
                check = invalid(must, passport[must])
                if check:
                    OK = False
                else:
                    continue

        if OK:
            print(passport, "returned: ", check)
            nbr_valid_pass = nbr_valid_pass + 1

    return nbr_valid_pass


def invalid(key, value):
    ret = True
    if key == "byr":
        # print(key, " ", value)
        if len(value) == 4:
            if int(value) in range(1920, 2003):
                ret = False

    elif key == "iyr":
        if len(value) == 4:
            if int(value) in range(2010, 2021):
                ret = False

    elif key == "eyr":
        if len(value) == 4:
            if int(value) in range(2020, 2031):
                return False

    elif key == "pid":
        if len(value) == 9 and value.isdigit():
            return False

    elif key == "hgt":
       if "cm" in value:
           s = value.split("cm")[0]
           if int(s) in range(150, 194):
               return False
       elif "in" in value:
           s = value.split("in")[0]
           if int(s) in range(59, 77):
               return False

    elif key == "ecl":
       if len(value) == 3:
          if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
               return False

    elif key == "hcl":
        if '#' in value:
            s = value.split('#')[1]
            if len(s) == 6:
                for char in s:
                    if char.isdigit():
                        if int(char) in range(0, 10):
                            continue
                        else:
                            return True

                    elif ord(char) in range(ord('a'), ord('g')):
                        continue
                    else:
                        return True

                return False

    return ret



def read_file(file_name):
    file = open(file_name, "r") #opens the file in read mode
    words = file.read().split("\n\n") #puts the file into an array
    file.close()
    return words

if __name__ == "__main__":
    nbr = valid_passports()
    print(nbr)
