import unittest
import time,sys
sys.path.append('./interface')
sys.path.append('./report')
import unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir,'*_test.py')

if __name__ =='__main__':

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    file_path = './report/'
    file_name = file_path + now + '_result.html'
    fp = open(file_name,'wb')

    runner = HTMLTestRunner(stream=fp,title='12',description='66')
    runner.run(discover)
    fp.close()

