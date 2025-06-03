def urlify(string: str) -> str:
    return "%20".join(string.split())


if __name__ == "__main__":
    print(urlify("asdd asdad "))
