import os
#本文件路径C:/Users/JHMK-ZSS/PycharmProjects/pyrequests/db_fixture/test_os.py
base_dir = os.path.dirname(__file__)
print(base_dir) #输出文件所在目录
base_dir1 = os.path.dirname(os.path.dirname(__file__))
print(base_dir1)#输出文件所在目录上一级目录
base_dir2 = os.path.abspath(__file__)
print(base_dir2)#输出文件所在位置绝对路径
base_dir3 = os.path.dirname(os.path.abspath(__file__))
print(base_dir3)#输出文件所在目录、
base_dir4 = os.getcwd()
print(base_dir4)#输出当前所在目录
base_dir5 = os.path.basename(__file__)
print(base_dir5)#输出文件名