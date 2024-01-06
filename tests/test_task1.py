import unittest
from task1.main import isEven, my_isEven


class TestTask1(unittest.TestCase):
    def test_isEven(self):
        self.assertEqual(isEven(12345.12), False)
        self.assertEqual(isEven(-3412.13), False)

        self.assertEqual(isEven(-123454242), True)
        self.assertEqual(isEven(-6436421), False)

        self.assertEqual(isEven(123456576868), True)
        self.assertEqual(isEven(1234598795864957), False)

    def test_my_isEven(self):
        self.assertEqual(my_isEven(12345.12), False)
        self.assertEqual(my_isEven(-3412.13), False)

        self.assertEqual(my_isEven(-123454242), True)
        self.assertEqual(my_isEven(-6436421), False)

        self.assertEqual(my_isEven(123456576868), True)
        self.assertEqual(my_isEven(1234598795864957), False)


if __name__ == '__main__':
    unittest.main()
