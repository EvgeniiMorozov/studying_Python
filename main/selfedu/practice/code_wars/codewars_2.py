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
        if sum(arr[i :]) == sum(arr[: i + 1]):
            return i
    return -1


# Task_8 - Vasya - Clerk

def tickets(people):
    if people[0] != 25:
        return 'NO'
    cash = 0
    for payment in people:
        if payment == 25:
            cash += 25
        else:
            if payment - 25 > cash:
                return 'NO'
            else:
                cash -= payment - 25
    return 'YES'



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
    print(find_even_index([1,100,50,-51,1,1]))
    print(find_even_index([20,10,-80,10,10,15,35]))


if __name__ == "__main__":
    main()
