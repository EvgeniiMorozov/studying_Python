# Task-1 Duplicate Encoder - https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    string = str()
    for i in word.lower():
        string += "(" if word.lower().count(i) == 1 else ")"
    return string


# Task-2 Valid string - https://www.codewars.com/kata/52f3bb2095d6bfeac2002196/train/python


# def valid_word(seq, word):
#     for chunk in seq:
#         word = word.replace(chunk, "")
#     return len(word) == 0


def valid_word(seq, word):
    for chunk in seq:
        temp_word = word.replace(chunk, "")
        temp_seq = seq.remove(chunk)
        for elem in temp_seq:
            temp_word = temp_word.replace(elem, "")

        if len(temp_word) == 0:
            return True
    return False


def main():
    # Task-1
    # print(duplicate_encode("din"))

    # Task-2
    print(valid_word(["code", "wars"], "codewars"))
    print(valid_word(["ab", "a", "bc"], "abc"))


if __name__ == "__main__":
    main()
