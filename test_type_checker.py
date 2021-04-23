import unittest
from type_checker import type_checker


class Demo(unittest.TestCase):

    def add_int(self, a: int, b: int) -> int:
        return a + b

    @type_checker()
    def add_int_with_check(self, a: int, b: int) -> int:
        return a + b

    def test_type_checker(self):
        demo = Demo()
        demo.assertEqual(3, demo.add_int(1, 2))  # OK
        demo.assertEqual('12', demo.add_int('1', '2'))  # nocheck, so just return '1' + '2'

        demo.assertEqual(3, demo.add_int_with_check(1, 2))  # OK
        demo.assertRaises(TypeError, demo.add_int_with_check, '1', '2')  # Raise the TypeError


if __name__ == '__main__':
    unittest.main()