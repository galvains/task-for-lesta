import time


def isEven(value):
    return value % 2 == 0


def my_isEven(value: int) -> bool:
    if isinstance(value, int):
        tmp = value % 10
        hs_table = {
            0: True,
            1: False,
            2: True,
            3: False,
            4: True,
            5: False,
            6: True,
            7: False,
            8: True,
            9: False,
        }
        return hs_table[tmp]
    else:
        return False


if __name__ == '__main__':

    value = 32145.2
    current_time = time.time()
    print(f"Предложенный алгоритм: {isEven(value)} | {round((time.time() - current_time) * 1000, 7)}")

    current_time = time.time()
    print(f"Модифицированный алг.: {my_isEven(value)} | {round((time.time() - current_time) * 1000, 7)}")
