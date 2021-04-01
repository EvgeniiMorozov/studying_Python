def checkio(text: str) -> str:

    letters = [el.lower() for el in list(filter(lambda i: i.lower().isalpha(), text))]
    lst = [(el, letters.count(el)) for el in set(letters)]
    dct = dict(sorted(lst, key=lambda i: i[1], reverse=True))
    values = list(dct.values())
    keys = list(dct.keys())

    if values.count(values[0]) == 1:

        return keys[0]

    else:
        temp_indices = list(filter(lambda i: values[i] == values[0], range(len(values))))

        return sorted([keys[i] for i in temp_indices])[0]


'''
def checkio(text: str) -> str:
    text = text.lower()
    r = {x: text.count(x) for x in text if x.isalpha()}

    return sorted([key for key in r if r[key] == max(r.values())])[0]
'''
