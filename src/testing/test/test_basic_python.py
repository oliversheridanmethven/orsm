import unittest


class TestBasicUnitTests(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(True, True)
    def test_fail(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
