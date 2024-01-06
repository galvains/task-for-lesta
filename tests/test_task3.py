import unittest
import random

from task3.main import counting_sort


def is_sorted(seq: list) -> bool:
    """ Функция сравнения результатов сортировки со стандартным методом сортировки sorted (Timsort).
    :param seq: отсортированный список с помощью counting_sort
    :return: True, в случае совпадения сортировок. Иначе - False.
    """
    if seq == sorted(seq):
        return True
    return False


class TestTask3(unittest.TestCase):
    seq1 = [random.randint(1, 100) for _ in range(100000)]
    seq2 = [random.randint(1, 10) for _ in range(1000)]
    seq3 = [random.randint(1, 150) for _ in range(20000)]
    seq4 = [random.randint(1, 1000) for _ in range(100)]
    seq5 = [random.randint(1, 1000) for _ in range(2000)]
    seq6 = [random.randint(1, 300) for _ in range(40000)]
    seq7 = [random.randint(1, 15000) for _ in range(20000)]
    seq8 = [random.randint(1, 100000) for _ in range(10)]

    def test_counting_sort(self):
        self.assertTrue(is_sorted(counting_sort(self.seq1)))
        self.assertTrue(is_sorted(counting_sort(self.seq2)))
        self.assertTrue(is_sorted(counting_sort(self.seq3)))
        self.assertTrue(is_sorted(counting_sort(self.seq4)))
        self.assertTrue(is_sorted(counting_sort(self.seq5)))
        self.assertTrue(is_sorted(counting_sort(self.seq6)))
        self.assertTrue(is_sorted(counting_sort(self.seq7)))
        self.assertTrue(is_sorted(counting_sort(self.seq8)))

    def test_static_counting_sort(self):
        self.assertEqual(counting_sort([3, 4, 5, 67, 8, 3, 2, 3, 45, 6]), [2, 3, 3, 3, 4, 5, 6, 8, 45, 67])
        self.assertEqual(counting_sort([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]),
                         [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6])
        self.assertEqual(counting_sort([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(counting_sort([0, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
