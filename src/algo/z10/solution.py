
def check_signs(word: str) -> int:
    max_l = 0
    current_l = 0
    sign = None
    start_list = [*word]
    for i, x in enumerate(start_list[2::]):
        if x == '<':
            current_l = current_l + 1 if sign == '<' else (sign := '<') and 1
        elif x == '>':
            current_l = current_l +1 if sign == '>' else (sign := '>') and 1
            # w celu objaśnienia góry, u doły stos if
            # if sign == '>':
            #     current_l += 1
            # else:
            #     sign = '>'
            #     current_l = 1
        if current_l > max_l:
            max_l = current_l

    return max_l

if __name__ == '__main__':
    word = 's = >>>>>><<<<<<>>>><'
    print(check_signs(word))