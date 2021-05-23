# Task_1 - N smallest elements in original order


def first_n_smallest(arr, n):
    if n == 0:
        return []
    elif len(arr) == n:
        return arr
    else:
        lst = sorted(list(set(arr)))
        indices = []
        for element in lst:
            indices += list(filter(lambda i: arr[i] == element, range(len(arr))))
        return [arr[i] for i in sorted(indices[:n])]


"""
def first_n_smallest(arr, n):
    lst = sorted(enumerate(arr), key=lambda it: it[1])[:n]
    lst.sort(key=lambda it:it[0])
    return [v for _,v in lst]

def first_n_smallest(arr, n):
    m = sorted(arr)[:n]
    return [m.pop(m.index(i)) for i in arr if i in m]
"""


# Task_2 - Leaderboard climbers


def leaderboard_sort(leaderboard, changes):

    for chunk in changes:
        name = chunk.split()[0]
        rank_change = chunk.split()[1]
        current_rank = leaderboard.index(name)

        if "+" in rank_change:
            feature_rank = current_rank - int(rank_change.replace("+", ""))
        else:
            feature_rank = current_rank + int(rank_change.replace("-", ""))

        temp = leaderboard.pop(current_rank)
        leaderboard.insert(feature_rank, temp)

    return leaderboard


"""
def leaderboard_sort(leaderboard, changes):
    for change in changes:
        name, delta = change.split()
        idx = leaderboard.index(name)
        leaderboard.insert(idx - int(delta), leaderboard.pop(idx))
    return leaderboard
"""


# Task_3 - Inside Out Strings


def inside_out(string):
    new_list = []
    for word in string.split():
        length = len(word)
        if length <= 3:
            new_list.append(word)
        else:
            if length % 2 == 0:
                new_word = word[: int(length / 2)][::-1] + word[int(length / 2) :][::-1]
            else:
                chunk = word[int(length / 2) : -2]
                new_word = (
                    word[: int(length / 2)][::-1]
                    + chunk[: int(len(chunk) / 2)][::-1]
                    + word[-1]
                    + chunk[int(len(chunk) / 2) :][::-1]
                )
            new_list.append(new_word)
    return " ".join(new_list)


# Task_4 - Sums of Parts


def parts_sums(sequence):
    if len(sequence) == 0:
        return [0]
    result = [0]
    acc = 0
    for el in reversed(sequence):
        acc += el
        result.insert(0, acc)
    return result


# Task_5 - Counting Duplicates


def duplicate_count(text):
    if len([el.lower() for el in text]) == len({el.lower() for el in text}):
        return 0
    list_of_duplicates = list(filter(lambda x: [el.lower() for el in text].count(x) > 1, {el.lower() for el in text}))
    return len(list_of_duplicates)


"""
def duplicate_count(s):
      return len([c for c in set(s.lower()) if s.lower().count(c)>1])
"""


# Task_6 - Find The Parity Outlier


def find_outlier(integers):
    remapped = ["even" if num % 2 == 0 else "odd" for num in integers]
    return integers.pop(remapped.index("even")) if remapped.count("even") == 1 else integers.pop(remapped.index("odd"))


"""
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
"""


# Task_7 - Equal Sides Of An Array


def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[i:]) == sum(arr[: i + 1]):
            return i
    return -1


# Task_8 - Vasya - Clerk


def tickets(people):
    if people[0] != 25:
        return "NO"
    cash = 0
    for payment in people:
        if payment == 25:
            cash += 25
        else:
            if payment - 25 > cash:
                return "NO"
            else:
                cash -= payment - 25
    return "YES"


# Task_9 - Moving Zeros To The End


def move_zeros(array):
    count_zeros = array.count(0)
    return list(filter(lambda x: x != 0, array)) + [0 for _ in range(count_zeros)]


# Task_10 - RGB To Hex Conversion


def rgb(r, g, b):

    arr = r, g, b
    result = []

    for i in arr:

        if 0 <= i <= 255:
            buffer = hex(i).replace("0x", "").upper()
            result.append(buffer if len(buffer) == 2 else "0" + buffer)

        elif i < 0:
            result.append("00")

        else:
            result.append("FF")

    return "".join(result)


"""
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""


# Task_11 - First non-repeating character


def first_non_repeating_letter(string):

    if len(string) == 0:
        return ""

    for i in string:
        if [el.lower() for el in string].count(i.lower()) == 1:
            return i

    return ""


# Task_12 - Simple Pig Latin


def pig_it(text):
    return " ".join(word[1:] + word[0] + "ay" if word.isalnum() else word for word in text.split())


# Task_13 - Detect Pangram

import string


def is_pangram(s):
    template = list(filter(lambda x: x.lower() in string.ascii_lowercase, s))
    buffer = list(string.ascii_lowercase)
    for el in template:
        if el.lower() in buffer:
            buffer.remove(el.lower())
    return len(buffer) == 0


"""
def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""


# Task_14 - Roman Numerals Encoder


def solution_1(number):
    template = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    digit = len(str(number))
    array = []
    for i in reversed(range(digit)):
        # print(i)
        divider = 10 ** i
        print(divider)
        array.append(number // 10 ** i)
        number %= 10 ** i
    print(array)
    return number


# Task_15 - Create Phone Number


def create_phone_number(array):
    array = [str(el) for el in array]
    return f"({''.join(array[:3])}) {''.join(array[3:6])}-{''.join(array[6:])}"


"""
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
"""


# Task_16 - Strip Comments


def solution(string, markers):
    sep = "\n"
    sep_indices = list(filter(lambda i: sep == string[i], range(len(string))))
    markers_indices = list(filter(lambda i: string[i] in markers, range(len(string))))

    result = []
    buffer = []
    is_writable = markers_indices[0] != 0

    for i in range(len(string)):
        if is_writable and i in markers_indices:
            result.append("".join(buffer).rstrip())
            is_writable = False
            buffer.clear()
        elif not is_writable and i in sep_indices:
            buffer.append(string[i])
            is_writable = True
        elif is_writable:
            buffer.append(string[i])

    result.append("".join(buffer).rstrip())
    return " ".join(result).rstrip()


# Task_17 - Range Extraction


def solution_2(args):

    buffer = []
    result = []

    j = args[0]

    for i in range(len(args)):

        if args[i] == j:
            buffer.append(str(args[i]))
        else:
            j = args[i]

            if 0 < len(buffer) <= 2:
                result.append("".join(buffer))
                buffer.clear()
            elif len(buffer) >= 3:
                result.append(f"{buffer[0]}-{buffer[-1]}")
                buffer.clear()

            result.append(str(args[i]))

        j += 1

    return result


def main():
    # Task_1
    # print(first_n_smallest([2, 1, 2, 3, 4, 2], 4))

    # Task_2
    # print(leaderboard_sort(["John", "Brian", "Jim", "Dave", "Fred"], ["Dave +1", "Fred +4", "Brian -1"]))

    # Task_3
    # print(inside_out("man i need a taxi up to ubud"))

    # Task_4
    # print(parts_sums([1, 2, 3, 4, 5, 6]))

    # Task_7
    # print(find_even_index([1,100,50,-51,1,1]))
    # print(find_even_index([20,10,-80,10,10,15,35]))

    # Task_9
    # print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

    # Task_10
    # print(rgb(148, 0, 211))

    # Task_11
    # print(first_non_repeating_letter("Go hang a salami, I'm a lasagna hog!"))

    # Task_12
    # print(pig_it("Quis custodiet ipsos custodes ?"))

    # Task_13
    # print(is_pangram("The quick, brown fox jumps over the lazy dog!"))

    # Task_14
    # print(solution_1(1883))

    # Task_15
    # print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

    # Task_16
    # print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

    # Task_17
    print(solution_2([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))


if __name__ == "__main__":
    main()
