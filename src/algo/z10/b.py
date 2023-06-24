def signs_list(word: str) -> list:
    start_list = [*word]
    def_val = 5
    res = []
    for i, x in enumerate(start_list):
        if x == '>':
            def_val -= 1
            res.append(def_val)
        if x == '<':
            def_val += 1
            res.append(def_val)

    return res


if __name__ == '__main__':
    words = '><<<>>><>>>><><>>>'
    print(signs_list(words))
