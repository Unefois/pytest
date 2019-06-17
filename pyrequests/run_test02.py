import sys,time
sys.path.append('./interface')
sys.path.append('./report')
import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,'*_test.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    file_name = './report/' + now + '_result.html'
    fb = open(file_name,'wb')
    runner = HTMLTestRunner(stream=fb,title='kuaidiinteface',description='kuaidkuaidi')
    runner.run(discover)
    fb.close()