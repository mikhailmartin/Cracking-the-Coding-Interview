from collections import Counter


def is_palindrome_permutation(string: str) -> bool:

    counter = Counter()
    for char in string:
        counter[char] += 1

    seen_solo = False
    for count in counter.values():
        if count % 2 == 1:
            if seen_solo:
                return False
            seen_solo = True
    return True


if __name__ == "__main__":
    print(is_palindrome_permutation("anna"))
    print(is_palindrome_permutation("aann"))
    print(is_palindrome_permutation("ana"))
    print(is_palindrome_permutation("aan"))
    print(is_palindrome_permutation("abc"))
