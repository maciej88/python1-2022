from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    seed(111)
    array1 = [randint(0, 10 ** 4) for _ in range(data_size)]
    array2 = [randint(0, 10 ** 4) for _ in range(data_size)]
    return [array1, array2]


def solve_problem(data):
    array1 = data[0]
    array2 = data[1]
    result = []
    for i in range(len(array1)):
        row = []
        for j in range(len(array2)):
            calc = array2[j] / array1[i]
            if calc.is_integer():
                row.append(calc)
        return result.append(len(row))


def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 10000:
        print(f'testing solver for {size=}')
        data = generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            result = solver(data)
            en = datetime.now().timestamp()
            time_sum += (en - st)

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10 ** 6)
        size *= 2

    return sizes, times


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve_problem)

    plt.plot(x, y)
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.show()
