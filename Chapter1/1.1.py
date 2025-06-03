def is_unique(string: str) -> bool:

    seen_chars = set()
    for char in string:
        if char in seen_chars:
            return False
        else:
            seen_chars.add(char)
    return True


if __name__ == "__main__":
    print(is_unique("aboba"))
