def compression(string: str) -> str:

    if string == "":
        return ""

    result = []
    prev_char = string[0]
    count = 1
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{prev_char}{count}")
            prev_char = char
            count = 1
    result.append(f"{prev_char}{count}")

    result = "".join(result)

    if len(string) <= len(result):
        return string
    else:
        return result


if __name__ == "__main__":
    print(compression("aabcccccaaa"))
    print(compression("abc"))
