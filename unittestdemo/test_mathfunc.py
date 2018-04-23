import unittest
from mathfunc import *
#在引用同目录的文件时，pycharm不会将当前文件目录自动加入自己的sourse_path。右键make_directory as-->Sources Root将当前工作的文件夹加入source_path就可以了。
class TestMathFunc(unittest.TestCase):
    '''Test mathfunc.py'''
    def test_add(self):
        '''Test menthod add(a,b)'''
        self.assertEqual(3,add(1,2))
        # self.assertEqual(3,add(2,2))

    def test_sub(self):
        self.assertEqual(1,sub(3,2))

    def test_multi(self):
        self.assertEqual(6,multi(2,3))

    def test_divide(self):
         self.assertEqual(3,divide(5,2))

if __name__ == '__main__':
    unittest.main()