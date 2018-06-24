import unittest
from arraylist import arraylist as a


class MyTest(unittest.TestCase):

    # Test make array method
    def test1(self):
        array = a.ArrayList()
        length = 0

        self.assertEqual(length, array.length())

    def test2(self):
        array = a.ArrayList()
        for i in range(5):
            array.add(i)
        length = 5
        self.assertEqual(length, array.length())

    def test3(self):
        array = a.ArrayList()
        length = 10
        for i in range(length):
            array.add(i)

        self.assertEqual(length, array.length())

    def test4(self):
        array = a.ArrayList()
        for i in range(5):
            array.add(i)
        self.assertEqual(array.get(4), 4)

    def test5(self):
        array = a.ArrayList()
        for i in range(5):
            array.add(i)

        self.assertEqual(array.get(0), 0)

    def test6(self):
        array = a.ArrayList()
        for i in range(5):
            array.add(i)

        self.assertRaises(array.get(10), IndexError('Index out of bound'))


if __name__ == '__main__':
    unittest.main()
