
"""
****     #
*     ####
*       ##
***     ##
*     ####
**     ###

jeśli długości *'ek klucza + długości #'ów zamka są dla wszystkich takie same, to klucz otwiera zamek3


"""




def open_lock(key: list[int], lock: list[int]) -> int:
    # sprawdzenie czy wartości nie są < 0
    if any(x < 0 for x in key) or any(x < 0 for x in lock):
        return -1    
    
    #proba otworzenia zamka
    key_index = 0
    lock_index = 0
    while key_index < len(key) and lock_index < len(lock):
        if key[key_index] == lock[lock_index]:
            key_index += 1
            lock_index += 1
        else:
            key_index += 1
    result = ""
    if lock_index == len(lock):
        result = "poprawny klucz"
        return result  #zamek sie otwiera
    else:
        result = "nie możesz wejść, zły klucz"
        return result  #zamek sie otwiera

# mały test
key = [2,3,4]
lock = [2,3,4]

print(open_lock(key,lock))