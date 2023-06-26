import time
from complete_scan_thru_subsequences import get_bin_representation


"""
UWAGA!
TEST WYKONUJESZ NA WŁASNĄ ODPOWIEDZIALNOŚĆ!
"""

def sequence_time_calculation(questions: list[int]) -> None:
    st = time.time()
    for N in questions:
        print(f"dla N = {N}")
        list_val = []
        for mask in range(2 ** N):
            maska = get_bin_representation(mask, N)
            for item_position in range(N):
                list_val.append(item_position) if maska[item_position] == "1" else None
        et = time.time()
        print(f"czas: {et - st}")
    return None


if __name__ == '__main__':
    # nie testuj powyżej 20!!!
    questions = [10, 20]
    print(sequence_time_calculation(questions))
