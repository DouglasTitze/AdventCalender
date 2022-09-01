def sort_str(input_string: str) -> str:
    return "".join(sorted(input_string))


def formatted_input():
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            inp, out = line.strip().split(" | ")
            yield (map(sort_str, inp.split(" ")), map(sort_str, out.split(" ")))


# Check if all the characters in small_num are in scrambled_num
def check_small_in_big(smaller_num, scrambled_num):
    smaller_num = list(smaller_num)
    scrambled_num = list(scrambled_num)

    for char in smaller_num:
        if char not in scrambled_num:
            return False

    return True


# Returns True if the
def is_five(smaller_num, scrambled_num):
    smaller_num = list(smaller_num)
    scrambled_num = list(scrambled_num)
    dif = 0

    for char in smaller_num:
        if char not in scrambled_num:
            dif += 1

    # If only one differnce than the number if 5
    if dif == 1:
        return True

    # Else it is 2
    else:
        return False


# Decode 1,4,7, and 8
def decode_display_easy(scrabled_num, dic):
    len_num = len(scrabled_num)
    if len_num == 2:
        dic["1"] = scrabled_num

    elif len_num == 4:
        dic["4"] = scrabled_num

    elif len_num == 3:
        dic["7"] = scrabled_num

    elif len_num == 7:
        dic["8"] = scrabled_num


# Decode 0,3,6, and 9
def decode_display_hard(scrabled_num, dic):
    len_num = len(scrabled_num)
    if len_num == 6:
        if check_small_in_big(dic["4"], scrabled_num):
            dic["9"] = scrabled_num

        elif check_small_in_big(dic["7"], scrabled_num):
            dic["0"] = scrabled_num

        else:
            dic["6"] = scrabled_num

    elif len_num == 5:
        if check_small_in_big(dic["1"], scrabled_num):
            dic["3"] = scrabled_num


# Decode 2 and 5
def decode_display_two_or_five(scrabled_num, dic):
    if is_five(dic["6"], scrabled_num):
        dic["5"] = scrabled_num
    else:
        dic["2"] = scrabled_num


# Delete exisitng scrambled number from the input list
def del_existing_num(lst, dic):
    for val in dic.values():
        if val in lst:
            lst.remove(val)

    return lst


sum_outputs = 0

# Decode each line from input file and add the result to sum_outputs
for inp, out in formatted_input():
    inp = list(inp)
    out = list(out)

    # 0 : len = 6 and contains 7, but not 4
    # 1 : len = 2
    # 2 : len = 5 found by deduction
    # 3 : len = 5 and contains 1
    # 4 : len = 4
    # 5 : len = 5 and contains 6, but differs only on one segment (2 differs by 3 segments)
    # 6 : len = 6, but does not contain 4 or 7
    # 7 : len = 3
    # 8 : len = 7
    # 9 : len = 6 and contains 4

    decoded_display = {}

    # Decode the easy ones
    for scrabled_num in inp:
        decode_display_easy(scrabled_num, decoded_display)

    del_existing_num(inp, decoded_display)

    # Decode the hard ones
    for scrabled_num in inp:
        decode_display_hard(scrabled_num, decoded_display)

    del_existing_num(inp, decoded_display)

    # Decode the remaining (two or five)
    for scrabled_num in inp:
        decode_display_two_or_five(scrabled_num, decoded_display)

    # Flip the dictionary so scrambled outputs return the designated number on the diplay
    decoded_display = {val: key for key, val in decoded_display.items()}

    num_str = ""

    # Each output value is decoded seperately, so add each decoded number as a string to num_str
    for scrabled_num in out:
        num_str += decoded_display[scrabled_num]

    # Add the final decoded number to sum_outputs
    sum_outputs += int(num_str)


print(sum_outputs)
