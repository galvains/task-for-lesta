import time
from task1.main import isEven, my_isEven


def task1(values: list) -> str:
    """ Функция для явного сравнения времени работы двух алгоритмов.

    В каждой итерации цикла вычисляется время выполнения функции, с последующим добавлением в список.
    На вывод получаем строку из суммы элементов (времени работы) для каждого списка.

    * 1000 - для понятного вывода без степеней.
    :param values: список элементов для проверки на четность.
    :return: str
    """
    proposed_algorithm = list()
    my_algorithm = list()
    current_time = time.time()

    for val in values:
        isEven(val)
        proposed_algorithm.append((time.time() - current_time) * 1000)

    current_time = time.time()
    for val in values:
        my_isEven(val)
        my_algorithm.append((time.time() - current_time) * 1000)

    return f"Предложенный алгоритм: {round(sum(proposed_algorithm), 7)}\n" \
           f"Модифицированный алг.: {round(sum(my_algorithm), 7)}"


def main() -> None:
    small_list = [
        234562352314,
        2345234,
    ]
    medium_list = [
        234562352314,
        2345234,
        546745,
        42134,
        1,
        5647,
        34,
        2,
        87675867856,
    ]
    big_list = [
        234562352314,
        2345234,
        546745,
        42134,
        1,
        5647,
        34,
        2,
        87675867856,
        45363456345,
        2345476458,
        999,
        2345234,
        546745,
        34,
        2,
        87675867856,
        45363456345,
    ]

    print(f"Small list\n{task1(small_list)}")
    print(f"Medium list\n{task1(medium_list)}")
    print(f"Big list\n{task1(big_list)}")


if __name__ == '__main__':
    main()
