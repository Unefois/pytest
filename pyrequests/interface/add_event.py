import unittest
import requests
import os,sys
import json
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event"



    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload = {'eid':'','name':'',"limit1":'','status':'','address':'','start_time':''}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result['status'],10021)
        self.assertEqual(self.result['message'],'parameter error')

    # def test_add_event_eid_exist(self):
    #     '''id 已存在'''
    #     payload = {'id':1,'name':'xiaomi6',"limit1":12,'status':1,'address':'2','start_time':'2018-07-12 12:12:12','create_time':'2018-07-09 12:12:13'}
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'],10022)
    #     self.assertEqual(self.result['message'],'event id already exists')
    #
    # def test_add_event_name_exist(self):
    #     '''name 已存在'''
    #     payload ={'id':2,'name':'xiaomi7',"limit1":10,'status':1,'address':'3','start_time':'2018-04-09 13:12:12','create_time':'2018-07-09 12:12:14'}
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'],10023)
    #     self.assertEqual(self.result['message','event name already exists'])
    #
    # def test_add_event_data_type_error(self):
    #     '''时间格式错误'''
    #     payload = {'id':3,'name':'xiaomi8',"limit1":121,'status':1,'address':'4','start_time':'2018-05-09','create_time':'2018-07-09 12:12:15'}
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'],10024)
    #     self.assertIn('start_time format error',self.result['message'])
    #
    # def test_add_event_sucess(self):
    #     '''添加成功'''
    #     payload = {'id':4,'name':'xiaomi9',"limit1":122,'status':1,'address':'5','start_time':'2018-06-09 15:12:12','create_time':'2018-07-09 12:12:16'}
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'],200)
    #     self.assertEqual(self.result['message'],'add event success')

    def tearDown(self):
        pass


    if __name__ == '__main__':
        test_data.init_data()#初始化接口数据
        unittest.main()


