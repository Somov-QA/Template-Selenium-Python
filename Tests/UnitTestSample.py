import unittest


class UnitTestSample(unittest.TestCase):
    value1 = 100
    value2 = 200

    def test_value1(self):
        self.assertEqual(self.value1, 100, "value1 is not 100")
        print("test value1 - PASSED")

    def test_value2(self):
        self.assertEqual(self.value2, 200, "value2 is not 200")
        print("test value2 - PASSED")


if __name__ == '__main__':
    unittest.main()
