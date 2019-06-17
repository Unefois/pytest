import unittest
import time,sys
sys.path.append('./interface')
sys.path.append('./report')
from HTMLTestRunner import HTMLTestRunner

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    file_name = './report/' + now + '_result.html'
    fp = open(file_name,'wb')
    runner = HTMLTestRunner(stream=fp,title='123',description='456')
    runner.run(discover)
    fp.close()