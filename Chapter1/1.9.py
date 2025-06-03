def is_cyclic_shift(string1: str, string2: str) -> bool:

    if len(string1) == len(string2) != 0:
        return (string1 + string1).find(string2) != -1
    return False


if __name__ == "__main__":
    print(is_cyclic_shift("waterbottle", "erbottlewat"))
