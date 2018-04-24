import unittest
from mathfunc import *
#在引用同目录的文件时，pycharm不会将当前文件目录自动加入自己的sourse_path。右键make_directory as-->Sources Root将当前工作的文件夹加入source_path就可以了。
class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once.")


    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once too.")


    def setUp(self):
        print('start setUp')

    def tearDown(self):
        print('start teardown')

    def test_add(self):
        print('add')
        self.assertEqual(3,add(1,2))

    def test_sub(self):
        print('sub')
        self.assertEqual(1,sub(3,2))

    def test_multi(self):
        print('multi')
        self.assertEqual(6,multi(2,3))

    # @unittest.skip("I don't want to run this case.")
    def test_divide(self):
        print('divide')
        self.assertEqual(3,divide(5,2))

if __name__ == '__main__':
    unittest.main(verbosity=2)