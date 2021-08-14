from collections import Counter
from hashlib import sha256, md5
from string import printable
import time


PRINTABLE = printable


def decrypt_method_1(data):
    result = ""
    for hash_str in data:
        for char in PRINTABLE:
            if hash_str == md5(char.encode()).hexdigest():
                result += char
            elif hash_str == sha256(char.encode()).hexdigest():
                result += char


def decrypt_method_2(data):
    result = ""

    md5_dict = {}
    sha256_dict = {}
    for char in PRINTABLE:
        md5_dict[md5(char.encode()).hexdigest()] = char
        sha256_dict[sha256(char.encode()).hexdigest()] = char

    for hash_str in data:
        if hash_str in md5_dict:
            result += md5_dict[hash_str]
        elif hash_str in sha256_dict:
            result += sha256_dict[hash_str]

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(result)

    return result


def main():
    with open("submit_the_flag_that_is_here.txt") as f:
        data = f.read().split()

    # print(Counter(data).most_common(10))
    # st = time.time()
    # decrypt_method_1(data)
    # endt = time.time()
    # print(f"Worktime - {endt-st:.2f} s")

    st = time.time()
    decrypt_method_2(data)
    endt = time.time()
    print(f"Worktime - {endt-st:.2f} s")


if __name__ == "__main__":
    main()
