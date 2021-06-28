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


# Task-3 - Sort the number sequence - https://www.codewars.com/kata/5816b76988ca9613cc00024f/train/python
def sort_sequence(sequence):
    new_arr = []
    tmp = []
    for idx, el in enumerate(sequence):
        if el == 0 or idx == len(sequence) - 1:
            new_arr.append(sorted(tmp) + [0])
            tmp.clear()
        else:
            tmp.append(el)
    new_arr = sorted(new_arr, key=sum)
    result = []
    for arr in new_arr:
        result.extend(arr)
    return result


"""
from itertools import chain,groupby

def sort_sequence(s):
    return[*chain.from_iterable(sorted((sorted([*l])+[0]for c,l in groupby(s,key = 0..__eq__)if not c),key=sum))]

from itertools import groupby

def sort_sequence(sequence):
    return sum(sorted([sorted(y)+[0] for x,y in groupby(sequence, lambda x: x==0) if not x],key=sum),[])

from itertools import groupby, chain

def sort_sequence(sequence):
    return list(chain.from_iterable(sorted((sorted(grp) + [0] for k, grp in groupby(sequence, key=bool) if k), key=sum)))
"""

# Task-4 - Twice linear - https://www.codewars.com/kata/5672682212c8ecf83e000050
def dbl_linear(num):
    def _y(n):
        return 2 * n + 1

    def _z(n):
        return 3 * n + 1

    lst = [1]
    buffer = []
    while len(lst) < num:
        for el in lst:
            if el not in buffer:
                if _y(el) not in lst:
                    lst.append(_y(el))
                if _z(el) not in lst:
                    lst.append(_z(el))
                lst = sorted(lst)
                buffer.append(el)
    lst = sorted(lst)
    return lst[num]


# Task-5 - Dubstep - https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
def song_decoder(song: str):
    return (" ").join(song.replace("WUB", " ").split())


# Task-6 - Your order, please - https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python
def order(sentence: str):
    if len(sentence) == 0:
        return ""
    array = []
    for i in range(1, len(sentence.split()) + 1):
        for chunk in sentence.split():
            if str(i) in chunk:
                array.append(chunk)
    return " ".join(array)


def main():
    # Task-1
    # print(duplicate_encode("din"))

    # Task-2
    # print(valid_word(["code", "wars"], "codewars"))
    # print(valid_word(["ab", "a", "bc"], "abc"))

    # Task-3
    # print(sort_sequence([3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 4, 2, 8, 0]))
    # print(sort_sequence([3, 2, 1, 0, 5, 6, 4, 0, 1, 5, 3, 0, 2, 2, 2, 0]))
    # print(sort_sequence([2, 2, 2, 0, 5, 6, 4, 0, 1, 5, 3, 0, 3, 2, 1, 0]))

    # Task-4
    # print(dbl_linear(30))

    # Task-5
    # print(song_decoder("WUBAWUBWUBBWUBCWUB"))

    # Task-6
    print(order("4of Fo1r pe6ople g3ood th5e the2"))


if __name__ == "__main__":
    main()
