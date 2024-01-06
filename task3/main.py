import time
import random


def counting_sort(seq):
    min_val = min(seq)
    max_val = max(seq)
    k = (max_val - min_val + 1)

    tmp = [0] * k
    for i in seq:
        tmp[i - min_val] += 1
    counter = 0
    for i in range(0, k):
        for _ in range(tmp[i]):
            seq[counter] = i + min_val
            counter += 1

    return seq


if __name__ == '__main__':
    seq = [random.randint(1, 100) for _ in range(10000)]
    current_time = time.time()
    print(f"{counting_sort(seq)}\nВремя сортировки: {round(time.time() - current_time, 7)} сек.")
