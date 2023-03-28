"""
zadanie2:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" (bez przesiadek).

"""
from gen_train_data import generate_data


def is_connected(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    return ((a, b) in train_data or (b, a) in train_data)


if __name__ == '__main__':
    rr = generate_data(10)
    print(rr)
    print(is_connected(rr, 12, 13))
