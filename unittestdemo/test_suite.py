import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"),TestMathFunc("test_sub"),TestMathFunc("test_divide")]
    suite.addTests(tests)

    #运行结果直接输出到控制台
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    #运行结果输出到指定的txt文件中
    # with open('UnittestTextReport.txt','a') as f:
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)
    #运行结果生成Html报告
    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)