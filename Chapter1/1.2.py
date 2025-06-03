from collections import Counter


def is_permutation(string1: str, string2: str) -> bool:

    def get_counter(string: str) -> dict[str, int]:
        counter = Counter()
        for char in string:
            counter[char] += 1
        return counter

    counter1 = get_counter(string1)
    counter2 = get_counter(string2)

    return counter1 == counter2


if __name__ == "__main__":
    print(is_permutation("aboba", "aboab"))
    print(is_permutation("aboba", "abo"))
