"""
zadanie1:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
 połączeń wychodzących.

"""


def get_city_most_connections(train_data: list[tuple[int, int]]) -> int:
    count_dict = {}
    for i in train_data:
        if i[1] not in count_dict:
            count_dict[i[1]] = 1
        else:
            count_dict[i[1]] += 1

    return max(count_dict, key=count_dict.get)