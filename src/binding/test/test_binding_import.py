import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import binding
        binding.hello_world()
        binding.func(1,'foo')


if __name__ == '__main__':
    unittest.main()
