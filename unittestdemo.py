import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print ("setup")
    def test_something(self):
        print("test something")
        self.assertEqual(True, False)
    def test_anything(self):
        print("test anything")
        self.assertEqual(True, True)
    def tearDown(self):
        print("teardown")


if __name__ == '__main__':
    unittest.main()
