"""
zadanie3:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" z dokładnie jedną przesiadką, czyli czy istnieje para połączeń typu (a,c),(c,b).

"""
from gen_train_data import generate_data


def is_connected_with_stopover(train_data: list[tuple[int, int]], a: int, b: int):
    val = []
    for i in train_data:
        if a in i or b in i:
            val.append(i)
    print(val)
    for j, tupla1 in enumerate(val):
        for tupla2 in val[j + 1:]:
            if tupla1[1] == tupla2[0] and tupla1[1] != a and tupla1[1] != b and tupla2[0] != a and tupla2[0] != b:
                if (tupla1[0] == a and tupla2[1] == b) or (tupla1[0] == b and tupla2[1] == a):
                    return True
    return False


if __name__ == '__main__':
    rr = generate_data(10)
    print(rr)
    print(is_connected_with_stopover(rr, 13, 12))
