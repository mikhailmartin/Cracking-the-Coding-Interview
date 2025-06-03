def is_one_away(string1: str, string2: str) -> bool:

    length1 = len(string1)
    length2 = len(string2)

    if abs(length1 - length2) > 1:
        return False

    if length1 == length2:
        one_flag = False
        for char1, char2 in zip(string1, string2):
            if char1 != char2:
                if one_flag:
                    return False
                one_flag = True
        return True

    if length1 > length2:
        small, big = string2, string1
        small_length, big_length = length2, length1
    else:
        small, big = string1, string2
        small_length, big_length = length1, length2

    one_flag = False
    small_pointer = 0
    big_pointer = 0
    while small_pointer != small_length and big_pointer != big_length:
        char_small = small[small_pointer]
        char_big = big[big_pointer]
        if char_small != char_big:
            if one_flag:
                return True
            one_flag = True
            big_pointer += 1
        else:
            small_pointer += 1
            big_pointer += 1
    return True


if __name__ == "__main__":
    print(is_one_away("aaaa", "aaaa"))
    print(is_one_away("aaaa", "aaaab"))
    print(is_one_away("baaaa", "aaaa"))
    print(is_one_away("aaaa", "aa"))
