# Task-1 Duplicate Encoder - https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    string = str()
    for i in word.lower():
        string += "(" if word.count(i) == 1 else ")"
    return string


def main():
    # Task-1
    print(duplicate_encode("din"))


if __name__ == '__main__':
    main()
