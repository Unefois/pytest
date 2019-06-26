import requests
import unittest

class Dilicode(unittest.TestCase):
    '''地理编码接口'''
    def setUp(self):
        self.base_url = "http://api.map.baidu.com/geocoding/v3/"
    def tearDown(self):
        print(self.result)

    def test_get_dilicode_success(self):
        '''成功响应'''
        r = requests.get(self.base_url,params={'address':'北京市海淀区上地十街10号','ak':'UQWNceTeluBItGbBfNQIZAFnFO5ACKTp','callback':'showLocation','output':'json'})
        self.result = r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['result'][0]['precise'],1)

    def test_get_dilicode_ak_null(self):
        '''ak为空'''
        r = requests.get(self.base_url,params={'address':'北京市海淀区上地十街10号','output':'json','callback':'showLocation'})
        self.result = r.json()
        self.assertEqual(self.result['status'],101)
        self.assertEqual(self.result['message'],'AK参数不存在')



if __name__ == '__main__':
    unittest.main()
