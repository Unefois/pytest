import sys,time
sys.path.append('./interface')
from HTMLTestRunner import HTMLTestRunner
import unittest

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './report/' + now + '_result.html'
    fb = open(filename,'wb')
    runner = HTMLTestRunner(stream=fb,title='ABD',description='678')
    runner.run(discover)
    fb.close()
