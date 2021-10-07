import copy
import time
import random
import visualize


def selection_sort(arr):
    num_operations = 0
    length = len(arr)
    for i in range(length):
        minim = i
        for j in range(i + 1, length):
            if arr[j] < arr[minim]:
                minim = j
        num_operations += length - (i + 1)
        arr[i], arr[minim] = arr[minim], arr[i]
    return num_operations


def insertion_sort(arr):
    num_operations = 0
    length = len(arr)
    for i in range(1, length):
        j = i
        while (j > 0) and (arr[j] < arr[j - 1]):
            num_operations += 2
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    return num_operations


def shell_sort(arr):
    num_operations = 0
    interval = 1
    while interval < len(arr):
        num_operations += 1
        interval = 3 * interval + 1
    while interval > 0:
        num_operations += 1
        for outer in range(interval, len(arr)):
            val_insert = arr[outer]
            inner = outer
            while inner > interval - 1 and arr[inner - interval] >= val_insert:
                num_operations += 2
                arr[inner] = arr[inner - interval]
                inner = inner - interval
            arr[inner] = val_insert
        interval = (interval - 1) // 3
    return num_operations


def merge_sort(arr):
    num_operations = 0
    if len(arr) > 1:
        num_operations += 1
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        num_operations += merge_sort(left)
        num_operations += merge_sort(right)

        num_operations += merge(arr, left, right)
    return num_operations


def merge(arr, left, right):
    num_operations = 0
    i = j = k = 0

    while i < len(left) and j < len(right):
        num_operations += 2
        num_operations += 1
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        num_operations += 1
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        num_operations += 1
        arr[k] = right[j]
        j += 1
        k += 1
    return num_operations


def test():
    algorithms = [selection_sort, insertion_sort, shell_sort, merge_sort]
    powers = list(range(7, 15 + 1))

    # first_exp(algorithms, powers)
    # print('--------------------------------------')
    # second_exp(algorithms, powers)
    # print('--------------------------------------')
    # third_exp(algorithms, powers)
    # print('--------------------------------------')
    fourth_exp(algorithms, powers)


def fourth_exp(algorithms, powers):
    exp_num = 4

    timing = {}
    num_operations = {}
    for i in range(3):
        for power in powers:
            arr_size = 2 ** power
            arr = [random.randint(1, 3) for _ in range(arr_size)]
            for algo in algorithms:
                dict_key = (algo.__name__, power)
                start = time.time()
                cur_num_operations = algo(copy.deepcopy(arr))
                finish = time.time()
                cur_timing = (finish - start) * 1000
                timing[dict_key] = timing.get(dict_key, 0) + cur_timing
                num_operations[dict_key] = (num_operations.get(dict_key, 0)
                                            + cur_num_operations)
            print(f'{power} power done')
        print(f'{i} iteration done')
    for algo in algorithms:
        for power in powers:
            dict_key = (algo.__name__, power)
            timing[dict_key] = timing[dict_key] / 3
            num_operations[dict_key] = num_operations[dict_key] / 3

    power_timing = {'selection_sort': [],
                    'insertion_sort': [],
                    'shell_sort': [],
                    'merge_sort': []}
    power_operations = {'selection_sort': [],
                        'insertion_sort': [],
                        'shell_sort': [],
                        'merge_sort': []}
    for algo in algorithms:
        for power in powers:
            dict_key = (algo.__name__, power)
            power_timing[algo.__name__].append(timing[dict_key])
            power_operations[algo.__name__].append(num_operations[dict_key])
        with open(f'exp_{exp_num}.csv', 'a') as f:
            f.write(f'{algo.__name__},'
                    f'{",".join([str(num) for num in power_timing[algo.__name__]])},'
                    f'{",".join([str(num) for num in power_operations[algo.__name__]])}\n')

    visualize.visualize(powers, power_timing, power_operations, exp_num)


def third_exp(algorithms, powers):
    exp_num = 3

    timing = {}
    num_operations = {}
    for power in powers:
        arr_size = 2 ** power
        arr = list(range(arr_size))
        arr.reverse()
        for algo in algorithms:
            dict_key = (algo.__name__, power)
            start = time.time()
            cur_num_operations = algo(copy.deepcopy(arr))
            finish = time.time()
            cur_timing = (finish - start) * 1000
            timing[dict_key] = timing.get(dict_key, 0) + cur_timing
            num_operations[dict_key] = (num_operations.get(dict_key, 0)
                                        + cur_num_operations)
        print(f'Power {power}')

    power_timing = {'selection_sort': [],
                    'insertion_sort': [],
                    'shell_sort': [],
                    'merge_sort': []}
    power_operations = {'selection_sort': [],
                        'insertion_sort': [],
                        'shell_sort': [],
                        'merge_sort': []}
    for algo in algorithms:
        for power in powers:
            dict_key = (algo.__name__, power)
            power_timing[algo.__name__].append(timing[dict_key])
            power_operations[algo.__name__].append(num_operations[dict_key])
        with open(f'exp_{exp_num}.csv', 'a') as f:
            f.write(f'{algo.__name__},'
                    f'{",".join([str(num) for num in power_timing[algo.__name__]])},'
                    f'{",".join([str(num) for num in power_operations[algo.__name__]])}\n')

    visualize.visualize(powers, power_timing, power_operations, exp_num)


def second_exp(algorithms, powers):
    exp_num = 2

    timing = {}
    num_operations = {}
    for power in powers:
        arr_size = 2 ** power
        arr = list(range(arr_size))
        for algo in algorithms:
            dict_key = (algo.__name__, power)
            start = time.time()
            cur_num_operations = algo(copy.deepcopy(arr))
            finish = time.time()
            cur_timing = (finish - start) * 1000
            timing[dict_key] = timing.get(dict_key, 0) + cur_timing
            num_operations[dict_key] = (num_operations.get(dict_key, 0)
                                        + cur_num_operations)
        print(f'Power {power}')

    power_timing = {'selection_sort': [],
                    'insertion_sort': [],
                    'shell_sort': [],
                    'merge_sort': []}
    power_operations = {'selection_sort': [],
                        'insertion_sort': [],
                        'shell_sort': [],
                        'merge_sort': []}
    for algo in algorithms:
        for power in powers:
            dict_key = (algo.__name__, power)
            power_timing[algo.__name__].append(timing[dict_key])
            power_operations[algo.__name__].append(num_operations[dict_key])
        with open(f'exp_{exp_num}.csv', 'a') as f:
            f.write(f'{algo.__name__},'
                    f'{",".join([str(num) for num in power_timing[algo.__name__]])},'
                    f'{",".join([str(num) for num in power_operations[algo.__name__]])}\n')

    visualize.visualize(powers, power_timing, power_operations, exp_num)


def first_exp(algorithms, powers):
    exp_num = 1

    timing = {}
    num_operations = {}
    for i in range(5):
        for power in powers:
            arr_size = 2 ** power
            arr = [random.randint(1, arr_size) for _ in range(arr_size)]
            for algo in algorithms:
                dict_key = (algo.__name__, power)
                start = time.time()
                cur_num_operations = algo(copy.deepcopy(arr))
                finish = time.time()
                cur_timing = (finish - start) * 1000
                timing[dict_key] = timing.get(dict_key, 0) + cur_timing
                num_operations[dict_key] = (num_operations.get(dict_key, 0)
                                            + cur_num_operations)
            print(f'{power} power done')
        print(f'{i} iteration done')
    for algo in algorithms:
        for power in powers:
            dict_key = (algo.__name__, power)
            timing[dict_key] = timing[dict_key] / 5
            num_operations[dict_key] = num_operations[dict_key] / 5

    power_timing = {'selection_sort': [],
                    'insertion_sort': [],
                    'shell_sort': [],
                    'merge_sort': []}
    power_operations = {'selection_sort': [],
                        'insertion_sort': [],
                        'shell_sort': [],
                        'merge_sort': []}
    for algo in algorithms:
        for power in powers:
            dict_key = (algo.__name__, power)
            power_timing[algo.__name__].append(timing[dict_key])
            power_operations[algo.__name__].append(num_operations[dict_key])
        with open(f'exp_{exp_num}.csv', 'a') as f:
            f.write(f'{algo.__name__},'
                    f'{",".join([str(num) for num in power_timing[algo.__name__]])},'
                    f'{",".join([str(num) for num in power_operations[algo.__name__]])}\n')

    visualize.visualize(powers, power_timing, power_operations, exp_num)


test()
